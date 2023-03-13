from src.errors import error_responses, database_errors, auth_errors
from src.models.todos_model import TodoCreate, TodoUpdate
from src.dependencies import auth_deps
from src.database.todos import Todos

from fastapi import HTTPException


todos = Todos()


def create_todo(new_todo: TodoCreate, token: str):
	try:
		user_data = auth_deps.verify_token(token)

		data = todos.create_todo(new_todo, user_data)
	
	except auth_errors.UserIsBroken:
		raise error_responses.user_is_broken

	except Exception as exp:
		print(exp)
		raise error_responses.server_internal

	return {'is_todo_created': True, 'todo_new': data}


def get_all_todos(token:str):
	try:
		user_data = auth_deps.verify_token(token)

		data = todos.get_all_todos(user_data)

	except auth_errors.UserIsBroken:
		raise error_responses.user_is_broken

	except Exception as exp:
		print(exp)
		raise error_responses.server_internal

	return {'is_all_todo_got': True, 'todos_all': data}

def get_todo_by_id(id: int, token: str):
	try:
		user_data = auth_deps.verify_token(token)

		data = todos.get_todo_by_id(id, user_data)
	
	except auth_errors.UserIsBroken:
		raise error_responses.user_is_broken

	except database_errors.DocNotFound:
		raise error_responses.doc_isnt_exist(id)

	except Exception as exp:
		print(exp)
		raise error_responses.server_internal

	return {'is_todo_got': True, 'todo_got': data}


def delete_todo(id: int, token: str):
	try:
		user_data = auth_deps.verify_token(token)

		data = todos.delete_todo(id, user_data)
	
	except auth_errors.UserIsBroken:
		raise error_responses.user_is_broken

	except database_errors.DocNotFound:
		raise error_responses.doc_isnt_exist(id)

	except Exception as exp:
		print(exp)
		raise error_responses.server_internal

	return {'is_todo_deleted': True, 'todo_del': data}


def update_todo(id: int, update_todo: TodoUpdate, token: str):
	try:
		user_data = auth_deps.verify_token(token)

		todo_upd = todos.update_todo(id, update_todo, user_data)
	
	except auth_errors.UserIsBroken:
		raise error_responses.user_is_broken

	except database_errors.DocNotFound:
		raise error_responses.doc_isnt_exist(id)

	except database_errors.TodoIsComplete:
		raise error_responses.todo_is_complete

	except Exception as exp:
		print(exp)
		raise error_responses.server_internal


	return {'is_todo_updated': True,'todo_upd': todo_upd}



