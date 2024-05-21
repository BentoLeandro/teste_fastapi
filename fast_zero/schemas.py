from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr

from fast_zero.models import TodoState


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class UserList(BaseModel):
    users: list[UserPublic]


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


# será usado para validar os dados de entrada quando
# uma nova tarefa é criada.
class TodoSchema(BaseModel):
    title: str
    description: str
    state: TodoState


# será usado para validar os dados de saída quando uma
# tarefa é retornada em um endpoint.
class TodoPublic(BaseModel):
    id: int
    title: str
    description: str
    state: TodoState
    created_at: datetime
    updated_at: datetime


class TodoList(BaseModel):
    todos: list[TodoPublic]


class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: str | None = None
