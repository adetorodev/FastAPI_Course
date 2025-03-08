from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Session, SQLModel, select
from database import engine
from depedency import get_session, create_db_and_tables
from models import User


app = FastAPI()

SQLModel.metadata.create_all(engine)

SessionDep = Annotated[Session, Depends(get_session)]

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


# Crud operation
@app.post("/users/")
def create_user(user: User, session: SessionDep) -> User: # type: ignore
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@app.get("/users/")
def read_users(
    session: SessionDep, # type: ignore
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[User]:
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users


@app.get("/users/{user_id}")
def read_user(user_id: int, session: SessionDep) -> "User": # type: ignore
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user


@app.delete("/users/{user_id}")
def delete_user(user_id: int, session: SessionDep): # type: ignore
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"ok": True}