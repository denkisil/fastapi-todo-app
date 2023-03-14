from src.config.config import return_settings
from src.errors import upload_errors


from fastapi import UploadFile
from uuid import uuid4 as uuid
from pathlib import Path

env = return_settings()


def file_is_image(file_content_type: str):
	if file_content_type.startswith('image'):
		return True
	else:
		return False
		


def check_filesize(file: bytes):
	if len(file) > env.MAX_FILESIZE:
		return False

	return True


def valid_image(file_content_type: str, file: bytes):

	is_image = file_is_image(file_content_type)

	is_normal_filesize = check_filesize(file)

	if not is_image:
		raise upload_errors.FileIsntImage('file is not image')

	if not is_normal_filesize:
		raise upload_errors.FilesizeBiggerThan('filesize bigger than max filesize (4 mb)')

	return True


def create_image_filename(filename: str):

	file_ex = Path(filename).suffix

	filename = (str(uuid()) + file_ex).replace("-", "")

	return filename

