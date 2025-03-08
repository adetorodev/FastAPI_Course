from sqlmodel import Field, Session, SQLModel, create_engine, select


# class User(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     name: str = Field(index=True)
#     age: int | None = Field(default=None, index=True)
#     secret_name: str


class UserBase(SQLModel):
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    secret_name: str


class UserPublic(UserBase):
    id: int


class UserCreate(UserBase):
    secret_name: str


class UserUpdate(UserBase):
    name: str | None = None
    age: int | None = None
    secret_name: str | None = None