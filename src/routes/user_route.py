from src.models.users_model import UserCreate, UserUpdate, UserAuth
from src.dependencies import auth_deps
from src.handlers import user_handler

from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends


router = APIRouter(prefix="/users")


@router.post("/new")
def create_user_page(new_user: UserCreate):
	return user_handler.create_user(new_user)


@router.post("/auth")
def auth_user_page(auth_user: OAuth2PasswordRequestForm = Depends()):
	return user_handler.auth_user(auth_user)


@router.delete("/user_delete")
def delete_account_page(token: str = Depends(auth_deps.oauth2_scheme)):
	return user_handler.delete_account(token)