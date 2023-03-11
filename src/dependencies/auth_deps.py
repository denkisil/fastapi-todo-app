from src.errors import auth_errors, database_errors, error_responses
from src.config.config import return_settings
from src.database.users import Users

from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from passlib.hash import bcrypt
from jose import jwt

users = Users()

env = return_settings()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/users/auth")


def check_password(password: str, password_hash: str):
	password_is_valid = bcrypt.verify(password, password_hash)

	if not password_is_valid:
		raise auth_errors.PasswordsIsntMatch("passwords isn't match")

	return True


def gen_token(payload: dict):
	to_encode = payload.copy()

	to_encode.update({'exp': datetime.utcnow() + timedelta(milliseconds=env.JWT_EXPIRES_AT)})

	token = jwt.encode(to_encode, env.JWT_SECRET)
	
	return token


def decode_token(token: str):
	data = jwt.decode(token, env.JWT_SECRET)

	return data


def user_is_exist(user: dict):
	try:
		is_user_exists = users.get_user_by_id(user['id'])
	except database_errors.DocNotFound:
		return False

	return True

def verify_token(token: str):
	
	user_data = decode_token(token)

	is_user_exists = user_is_exist(user_data)

	if not is_user_exists:
		raise auth_errors.UserIsBroken('user with this id is broken')

	return user_data
	
	