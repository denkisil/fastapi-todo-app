from src.models.todos_model import TodoCreate, TodoUpdate
from src.dependencies import auth_deps
from src.handlers import todos_handler

from fastapi.security import OAuth2PasswordBearer
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/todos")

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/users/login")


@router.get("/")
def get_all_todos_page(token: str = Depends(auth_deps.oauth2_scheme)):
	return todos_handler.get_all_todos(token)


@router.get("/{id}")
def get_todo_by_id_page(id: int, token: str = Depends(auth_deps.oauth2_scheme)):
	return todos_handler.get_todo_by_id(id, token)


@router.post("/new")
def create_todo_page(new_todo: TodoCreate, token: str = Depends(auth_deps.oauth2_scheme)):
	return todos_handler.create_todo(new_todo, token)


@router.put("/{id}")
def update_todo_page(id: int, update_todo: TodoUpdate, token: str = Depends(auth_deps.oauth2_scheme)):
	return todos_handler.update_todo(id, update_todo, token)


@router.delete("/{id}")
def delete_todo_page(id: int, token: str = Depends(auth_deps.oauth2_scheme)):
	return todos_handler.delete_todo(id, token)


