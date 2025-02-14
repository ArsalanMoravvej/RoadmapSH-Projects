from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import datetime
from typing import Annotated, Optional, List


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
        orm_mode = True

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
    title: str = Field(
        min_length=3,
        max_length=100,
        description="Task title must be between 3 and 100 characters"
    )
    description: str = Field(
        min_length=10,
        max_length=1000,
        description="Task description must be between 10 and 1000 characters"
    )
    status: int = Field(
        default=1,
        ge=1,
        le=3,
        description="Task status must be between 1 and 3"
    )
    priority: int = Field(
        default=5,
        ge=1,
        le=5,
        description="Task priority must be between 1 and 5"
    )


    @field_validator('title')
    def validate_title(cls, v):
        if v.strip() == "":
            raise ValueError("Title cannot be just whitespace")
        if not any(c.isalnum() for c in v):
            raise ValueError("Title must contain at least one alphanumeric character")
        return v.strip()

    @field_validator('description')
    def validate_description(cls, v):
        if v.strip() == "":
            raise ValueError("Description cannot be just whitespace")
        if not any(c.isalnum() for c in v):
            raise ValueError("Description must contain at least one alphanumeric character")
        return v.strip()


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
        orm_mode = True

class PaginatedTaskResponse(BaseModel):
    data: List[TaskResponse]
    total: int
    page: int
    limit: int

