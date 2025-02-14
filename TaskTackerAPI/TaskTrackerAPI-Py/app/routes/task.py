"""
Task management API routes.
This module defines the API endpoints for managing tasks, including retrieving,
creating, updating, and deleting tasks. The routes are defined using FastAPI's
APIRouter and include dependency injection for database sessions and user authentication.
Routes:
    - GET /tasks: Retrieve all tasks with optional filtering, pagination, and search.
    - GET /tasks/{id}: Retrieve a specific task by its ID.
    - POST /tasks: Create a new task.
    - DELETE /tasks/{id}: Delete a task by its ID.
    - PUT /tasks/{id}: Update a task by its ID.
Dependencies:
    - db: Database session dependency.
    - current_user: User authentication dependency.
Models:
    - models.Task: Task model representing a task in the database.
    - models.User: User model representing a user in the database.
Schemas:
    - schemas.PaginatedTasksResponse: Response schema for paginated tasks.
    - schemas.TaskResponse: Response schema for a single task.
    - schemas.TaskCreate: Request schema for creating a new task.
    - schemas.TaskUpdate: Request schema for updating an existing task.
Exceptions:
    - HTTPException: Raised for various HTTP errors, such as 404 Not Found and 403 Forbidden.
"""

from fastapi import Response, status, HTTPException, Depends, APIRouter, Query
from .. import models, schemas, oauth2

from ..database import get_db
from sqlalchemy.orm import Session

from typing import Optional
from datetime import datetime, timezone

router = APIRouter(
    prefix="/tasks",
    tags=['Tasks']
)

# Retrieve all tasks (Filtered)
@router.get("/",
            response_model=schemas.PaginatedTasksResponse
            )
async def get_tasks(db: Session = Depends(get_db),
                    limit: int = Query(10, gt=0),
                    page: int = Query(1, ge=1),
                    search: Optional[str] = Query(None),
                    current_user: models.User = Depends(oauth2.get_current_user)):

    if search:
        tasks = db.query(models.Task).filter(models.Task.title.ilike(f"%{search}%"),
                                            models.Task.owner_id == current_user.id,
                                            models.Task.is_deleted == False)
    else:
         tasks = db.query(models.Task).filter(models.Task.owner_id == current_user.id,
                                            models.Task.is_deleted == False)
    
    total  = tasks.count()
    offset = limit * (page - 1) 
    filtered_tasks = tasks.offset(offset).limit(limit).all()

    return {
        "data": filtered_tasks,
        "page": page,
        "limit": limit,
        "total": total
        }

# Retrieve a specific task given its ID
@router.get("/{id}", response_model=schemas.TaskResponse)
async def get_task(id: int,
                   db: Session = Depends(get_db),
                   current_user: models.User = Depends(oauth2.get_current_user)):

    task = db.query(models.Task).filter(models.Task.id == id,
                                        models.Task.is_deleted == False).first()
    
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Task with ID {id} was not found.")
    
    if task.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action on task with ID: {id}.")
    
    return task

# Create a new Task
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.TaskResponse)
async def create_task(task: schemas.TaskCreate,
                      db:Session = Depends(get_db),
                      current_user: models.User = Depends(oauth2.get_current_user)):

    new_task = models.Task(
        **task.model_dump(),
        owner_id=current_user.id)

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

# Delete a task given its ID
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(id: int,
                      db:Session = Depends(get_db),
                      current_user: models.User = Depends(oauth2.get_current_user)):
    
    task_query = db.query(models.Task).filter(models.Task.id == id,
                                              models.Task.is_deleted == False)
    task_obj = task_query.first()
    
    if task_obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Task with ID {id} was not found.")
    
    if task_obj.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action on task with ID: {id}.")
    
    task_query.update({"is_deleted": True, "deleted_at": datetime.now(timezone.utc)}, synchronize_session=False)

    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Update a task given its ID
@router.put("/{id}", response_model=schemas.TaskResponse)
async def update_task(id: int,
                      task: schemas.TaskUpdate,
                      db:Session = Depends(get_db),
                      current_user: models.User = Depends(oauth2.get_current_user)):
    
    task_query = db.query(models.Task).filter(models.Task.id == id,
                                              models.Task.is_deleted == False)
    task_obj = task_query.first()

    if task_obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Task with ID {id} was not found.")

    if task_obj.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action on task with ID: {id}.")

    task_query.update(
        {**task.model_dump(), "last_modified_at": datetime.now(timezone.utc)},
        synchronize_session=False
    )
    
    db.commit()

    return task_query.first()
