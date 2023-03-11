from src.models.users_model import UserCreate, UserUpdate
from src.database.database import Base
from src.errors import database_errors

from passlib.hash import bcrypt


class Users(Base):
	

	def __init__(self):
		super().__init__()


	def get_user_by_name(self, name: str):

		user_exist = self.db.table("users").select("*").eq("username", name).execute()

		if user_exist.data == []:
			raise database_errors.DocNotFound()

		return user_exist.data


	def get_user_by_id(self, id: int):

		user_exist = self.db.table("users").select("*").eq("id", id).execute()

		if user_exist.data == []:
			raise database_errors.DocNotFound()

		return user_exist.data


	def create_user(self, new_user: dict):

		user_exist = self.db.table("users").select("*").eq("username", new_user['username']).execute()

		if user_exist.data != []:
			raise database_errors.DocIsExist()

		new_user['password_hash'] = bcrypt.hash(new_user['password'])

		del new_user['password']

		user_created = self.db.table("users").insert(new_user).execute()

		return user_created.data


	def delete_user(self, user: dict):

		user_exist = self.db.table("users").select("*").eq("id", user['id']).execute()

		if user_exist.data == []:
			raise database_errors.DocNotFound()

		todos_deleted = self.db.table("todos").delete().eq("user_id", user['id']).execute()

		user_deleted = self.db.table("users").delete().eq("id", user['id']).execute()

		return user_deleted.data



