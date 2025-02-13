from fastapi  import status, HTTPException, Depends, APIRouter
from sqlalchemy.exc import IntegrityError
from .. import models, schemas, utils


from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

#User Registration Path
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
async def create_user(user: schemas.UserCreate, db:Session = Depends(get_db)):

    #hash the password
    hashed_pass = utils.hash(user.password)
    user.password = hashed_pass

    new_user = models.User(**user.model_dump())
    
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)  # Retrieve saved user details
        return new_user
    except IntegrityError:
        db.rollback()  # Undo the transaction
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )