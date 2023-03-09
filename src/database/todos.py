from src.models.todos_model import TodoCreate, TodoUpdate
from src.database.database import Base
from src.errors import database_errors

class Todos(Base):


	def __init__(self):
		super().__init__()


	def get_all_todos(self):

		all_todos = self.db.table("todos").select("*").execute()

		return all_todos.data


	def get_todo_by_id(self, id: int):

		todo_found = self.db.table("todos").select("*").eq("id", id).execute()

		if todo_found.data == []:
			raise database_errors.DocNotFound(f'cannot find doc by this id: {id}')

		return todo_found.data


	def create_todo(self, new_todo: TodoCreate):

		new_todo = dict(new_todo)

		data = self.db.table("todos").insert(new_todo).execute()

		return data.data


	def delete_todo(self, id: int):
			
		todo_found = self.db.table("todos").select("*").eq("id", id).execute()

		if todo_found.data == []:
			raise database_errors.DocNotFound(f'cannot find doc by this id: {id}')
			
		
		todo_del = self.db.table("todos").delete().eq("id", id).execute()

		return todo_del.data


	def update_todo(self, id: int, update_data: TodoUpdate):

		update_data = dict(update_data)

		data_to_update = dict()

		todo_found = self.db.table("todos").select("*").eq("id", id).execute()

		if todo_found.data == []:
			raise database_errors.DocNotFound(f'cannot find doc by this id: {id}')

		for key in update_data:
			if update_data[key] != None:
				data_to_update[key] = update_data[key]

		
		todo_upd = self.db.table("todos").update(data_to_update).eq("id", id).execute()

		return todo_upd.data


