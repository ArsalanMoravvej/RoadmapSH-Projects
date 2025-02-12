from fastapi  import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy import func
from .. import models, schemas, oauth2

from ..database import get_db
from sqlalchemy.orm import Session

from typing import Optional, List

router = APIRouter(
    prefix="/tasks",
    tags=['Tasks']
)

# Create a new Task
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.TaskResponse)
async def create_task(task: schemas.TaskCreate,
                      db:Session = Depends(get_db),
                      current_user: models.User = Depends(oauth2.get_current_user)):

    (print("here"))
    new_task = models.Task(
        **task.model_dump(),
        owner_id=current_user.id)

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

# Retrieve a specific task by ID
@router.get("/{id}", response_model=schemas.TaskResponse)
async def get_task(id: int,
                   db: Session = Depends(get_db),
                   current_user: models.User = Depends(oauth2.get_current_user)):

    task = db.query(models.Task).filter(models.Task.id == id).first()
    
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Task with ID {id} was not found.")
    
    if task.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action on task with ID: {id}.")
    
    return task

# Delete a task by ID
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(id: int,
                      db:Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)):
    
    task = db.query(models.Task).filter(models.Task.id == id)
    
    if task.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Task with ID {id} was not found.")
    
    if task.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action on task with ID: {id}.")
    
    task.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.TaskResponse)
async def update_task(id: int,
                      task: schemas.TaskCreate,
                      db:Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)):
    
    task_query = db.query(models.Task).filter(models.Task.id == id)

    if task_query.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Task with ID {id} was not found.")

    if task_query.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action on task with ID: {id}.")

    task_query.update(task.model_dump(), synchronize_session=False)
    
    db.commit()

    return task_query.first()
