from src.handlers import images_handler
from src.dependencies import auth_deps, image_deps

from fastapi import APIRouter, UploadFile, File, Depends
from uuid import uuid4 as uuid
import shutil
import os

router = APIRouter(prefix="/imgs")


@router.post('/upload')
def upload_image_page(new_image: UploadFile, token: str = Depends(auth_deps.oauth2_scheme)):
	return images_handler.upload_image(token, new_image)

	
