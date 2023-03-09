from src.models.todos_model import TodoCreate, TodoUpdate
from src.errors import database_errors
from src.database.todos import Todos

from fastapi import HTTPException


todos = Todos()


def create_todo(new_todo: TodoCreate):
	try:
		data = todos.create_todo(new_todo)
	except Exception as exp:
		print(exp)
		raise HTTPException(status_code=500, detail={'code': "E_SERVER_INTERNAL", 'msg': "something happens on server"})

	return {'is_todo_created': True, 'todo_new': data}


def get_all_todos():
	try:
		data = todos.get_all_todos()
	except Exception as exp:
		print(exp)
		raise HTTPException(status_code=500, detail={'code': "E_SERVER_INTERNAL", 'msg': "something happens on server"})

	return {'is_all_todo_got': True, 'todos_all': data}

def get_todo_by_id(id: int):
	try:
		data = todos.get_todo_by_id(id)
	except database_errors.DocNotFound:
		raise HTTPException(status_code=404, detail={'code': "E_NOT_FOUND", 'msg': f'cannot find doc by this id {id}'})
	except Exception as exp:
		print(exp)
		raise HTTPException(status_code=500, detail={'code': "E_SERVER_INTERNAL", 'msg': "something happens on server"})

	return {'is_todo_got': True, 'todo_got': data}


def delete_todo(id: int):
	try:
		data = todos.delete_todo(id)
	except database_errors.DocNotFound:
		raise HTTPException(status_code=404, detail={'code': "E_NOT_FOUND", 'msg': f'cannot find doc by this id {id}'})
	except Exception as exp:
		print(exp)
		raise HTTPException(status_code=500, detail={'code': "E_SERVER_INTERNAL", 'msg': "something happens on server"})

	return {'is_todo_deleted': True, 'todo_del': data}


def update_todo(id: int, update_todo: TodoUpdate):
	try:
		todo_upd = todos.update_todo(id, update_todo)
	except database_errors.DocNotFound:
		raise HTTPException(status_code=404, detail={'code': "E_NOT_FOUND", 'msg': f'cannot find doc by this id {id}'})
	except Exception as exp:
		print(exp)
		raise HTTPException(status_code=500, detail={'code': "E_SERVER_INTERNAL", 'msg': "something happens on server"})


	return {'is_todo_updated': True,'todo_upd': todo_upd}