from src.models.todos_model import TodoCreate, TodoUpdate
from src.handlers import todos_handler

from fastapi import APIRouter

router = APIRouter(prefix="/todos")


@router.get("/")
def all_todos_list_page():
	return todos_handler.all_todos_list()


@router.get("/{id}")
def get_todo_by_id_page(id: int):
	return todos_handler.get_todo_by_id(id)


@router.put("/{id}")
def update_todo_by_id_page(id: int, todo_update: TodoUpdate):
	return todos_handler.update_todo_by_id(id, todo_update)


@router.post("/new")
def add_todo_page(new_todo: TodoCreate):
	return todos_handler.add_todo(new_todo)


@router.delete("/{id}")
def delete_todo_by_id_page(id: int):
	return todos_handler.delete_todo_by_id(id)