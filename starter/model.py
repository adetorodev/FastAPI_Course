from typing import Optional, List
from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    male = "male",
    female = "female"

class Role(str, Enum):
    admin = "admin",
    student = "student",
    teacher = "teacher",

class User(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    email_address: str
    roles: List[Role]

class UpdateUser(BaseModel):
    first_name: str
    last_name: str
    gender: Gender