from src.models.todos_model import TodoCreate, TodoUpdate
from src.database.database import Todos

from playhouse.shortcuts import model_to_dict
from fastapi import HTTPException
from peewee import DoesNotExist


def add_todo(new_todo: TodoCreate):
	todo_to_create = Todos.create(title = new_todo.title, desc=new_todo.description)

	todo_to_create.save()

	return {'is_todo_created': True, 'todo': new_todo}


def all_todos_list():
	all_todos = [todo for todo in Todos.select().dicts()]

	return {'is_all_todos_got': True, 'todos': all_todos}


def get_todo_by_id(id: int):
	todo_got = model_to_dict(get_todo(id))

	return {'is_todo_got': True, 'todo_id': id, 'todo_got': todo_got}


def update_todo_by_id(id: int, update_todo: TodoUpdate):
	todo_to_update = model_to_dict(get_todo(id))

	for key, value in update_todo:
		if value != None:
			todo_to_update[key] = value

	Todos.update(**todo_to_update).where(Todos.id == id).execute()

	return {'is_todo_updated': True, 'todo_upd': todo_to_update}
		

def delete_todo_by_id(id: int):
	todo_to_delete = get_todo(id)

	todo_to_delete.delete_instance()

	return {'is_todo_deleted': True, 'todo_del': todo_to_delete.__data__}


def get_todo(id: int):
	try:
		todo_got = Todos.get(Todos.id==id)
		return todo_got
	except DoesNotExist:
		raise HTTPException(status_code=404, detail={'msg': 'cannot find document by id', 'code': 'E_NOT_FOUND'})
	except:
		raise HTTPException(status_code=500, detail={'msg': 'something happen on server', 'code': 'E_SERVER_INTERNAL'})
