from src.models.todos_model import TodoCreate, TodoUpdate
from src.database.database import Base
from src.database.users import Users
from src.errors import database_errors

class Todos(Base):


	def __init__(self):
		super().__init__()


	def get_all_todos(self, user: dict):

		all_todos = self.db.table("todos").select("*").eq('user_id', user['id']).execute()

		return all_todos.data


	def get_todo_by_id(self, id: int, user: dict):

		todo_found = self.db.table("todos").select("*").eq("id", id).eq("user_id", user['id']).execute()

		if todo_found.data == []:
			raise database_errors.DocNotFound(f'cannot find doc by this id: {id}')

		return todo_found.data


	def create_todo(self, new_todo: TodoCreate, user: dict):

		new_todo = dict(new_todo)

		new_todo['user_id'] = user['id']

		data = self.db.table("todos").insert(new_todo).execute()

		return data.data


	def delete_todo(self, id: int, user: dict):
			
		todo_found = self.db.table("todos").select("*").eq("id", id).eq("user_id", user['id']).execute()

		if todo_found.data == []:
			raise database_errors.DocNotFound(f'cannot find doc by this id: {id}')
			
		
		todo_del = self.db.table("todos").delete().eq("id", id).execute()

		return todo_del.data


	def update_todo(self, id: int, update_data: TodoUpdate, user: dict):

		update_data = dict(update_data)

		data_to_update = dict()

		todo_found = self.db.table("todos").select("*").eq("id", id).eq("user_id", user['id']).execute()

		if todo_found.data == []:
			raise database_errors.DocNotFound(f'cannot find doc by this id: {id}')

		if todo_found.data[0]['complete'] == True:
			raise database_errors.TodoIsComplete('cannot update completed todo')

		for key in update_data:
			if update_data[key] != None:
				data_to_update[key] = update_data[key]

		
		todo_upd = self.db.table("todos").update(data_to_update).eq("id", id).execute()

		return todo_upd.data


