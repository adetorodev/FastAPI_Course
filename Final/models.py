# from sqlmodel import Field, Session, SQLModel, create_engine, select


# class User(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     name: str = Field(index=True)
#     age: int | None = Field(default=None, index=True)
#     secret_name: str


# class UserBase(SQLModel):
#     name: str = Field(index=True)
#     age: int | None = Field(default=None, index=True)


# class User(UserBase, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     secret_name: str


# class UserPublic(UserBase):
#     id: int


# class UserCreate(UserBase):
#     secret_name: str


# class UserUpdate(UserBase):
#     name: str | None = None
#     age: int | None = None
#     secret_name: str | None = None


# =========== using mongo db model style ========
from typing import Optional, List # Supports for type hints
from pydantic import BaseModel # Most widely used data validation library for python
from enum import Enum # Supports for enumerations

# enum for gender
class Gender(str, Enum):
    male = "male"
    female = "female"

# enum for role
class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"
    teacher = "teacher"

class User(BaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = None  # Make middle name optional
    gender: Gender
    email_address: str
    phone_number: str
    roles: List[Role] # user can have several roles