from src.errors import error_responses, database_errors, auth_errors
from src.models.users_model import UserCreate, UserUpdate, UserAuth
from src.config.config import return_settings
from src.dependencies import auth_deps
from src.database.users import Users

from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from fastapi import HTTPException
from jose import JWTError


users = Users()

env = return_settings()


def create_user(new_user: UserCreate):
	try:
		user_created = users.create_user(dict(new_user))

		return {'is_user_created': True, 'user_new': user_created}
	except database_errors.DocIsExist:
		raise error_responses.user_exist(new_user.username)
		
	except Exception as exp:
		print(exp)
		raise error_responses.server_internal


def auth_user(auth_user: OAuth2PasswordRequestForm):
	try:

		user_exist = users.get_user_by_name(auth_user.username)[0]

		is_user_password_valid = auth_deps.check_password(auth_user.password, user_exist['password_hash'])

		del user_exist['password_hash']

		token = auth_deps.gen_token(user_exist)

		return {'is_auth_token_generated': True, 'access_token': token}

	except database_errors.DocNotFound:
		raise error_responses.user_isnt_exist(auth_user.username)

	except auth_errors.PasswordsIsntMatch:
		raise error_responses.password_is_invalid

	except Exception as exp:
		print(exp)
		raise error_responses.server_internal

def delete_account(token: str):
	try:
		user_data = auth_deps.verify_token(token)

		user_deleted = users.delete_user(user_data)

		return {'is_account_deleted': True, 'user_del': user_deleted}

	except auth_errors.UserIsBroken:
		raise error_responses.user_is_broken

	except Exception as exp:
		print(exp)
		raise error_responses.server_internal
	
