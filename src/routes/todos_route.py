from src.models.todos_model import TodoCreate, TodoUpdate
from src.handlers import todos_handler

from fastapi import APIRouter


router = APIRouter(prefix="/todos")


@router.get("/")
def get_all_todos_page():
	return todos_handler.get_all_todos()


@router.get("/{id}")
def get_todo_by_id_page(id: int):
	return todos_handler.get_todo_by_id(id)


@router.post("/new")
def create_todo_page(new_todo: TodoCreate):
	return todos_handler.create_todo(new_todo)


@router.put("/{id}")
def update_todo_page(id: int, update_todo: TodoUpdate):
	return todos_handler.update_todo(id, update_todo)


@router.delete("/{id}")
def delete_todo_page(id: int):
	return todos_handler.delete_todo(id)


