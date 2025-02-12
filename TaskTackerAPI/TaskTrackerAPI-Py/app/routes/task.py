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
async def create_task(post: schemas.TaskCreate,
                      db:Session = Depends(get_db),
                      current_user: models.User = Depends(oauth2.get_current_user)):

    (print("here"))
    new_task = models.Task(
        **post.model_dump(),
        owner_id=current_user.id)

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task