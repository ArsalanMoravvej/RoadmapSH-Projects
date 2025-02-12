from pydantic import BaseModel, EmailStr, Field, conint
from datetime import datetime
from typing import Annotated, Optional


# Define a models for request payload validation and serialization

# user schema base class
class UserBase(BaseModel):
    name: str
    email:    EmailStr

# user schema creation class
class UserCreate(UserBase):
    password: str

# user schema response class
class UserResponse(UserBase):
    id:         int
    created_at: datetime
    
    class Config:
        orm_mod = True

# user login class
class UserLogin(BaseModel):
    email:    EmailStr
    password: str

# jwt token base class
class Token(BaseModel):
    access_token: str
    token_type: str

# jwt token data class
class TokenData(BaseModel):
    id: Optional[str] | Optional[int] = None

# task base class
class TaskBase(BaseModel):
    title:     str
    content:   str
    status:    int

# task creation class
class TaskCreate(TaskBase):
    pass

# task response class
class TaskResponse(TaskBase):
    id:         int
    owner_id :  int
    owner: UserResponse 
    created_at: datetime
    
    class Config:
        orm_mod = True

