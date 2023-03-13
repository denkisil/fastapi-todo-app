from src.errors import error_responses, auth_errors, upload_errors
from src.dependencies import auth_deps, image_deps
from src.database.images import Images

from fastapi import UploadFile, File


images = Images()


def upload_image(token: str, new_image: UploadFile = File(...)):
	try:

		filename = new_image.filename

		filedata = new_image.file.read()

		user_data = auth_deps.verify_token(token)

		filename = image_deps.create_image_filename(filename)

		image_created = images.upload_image(filename, filedata, user_data)

		return {'is_image_uploaded': True, 'image_upl': image_created}

	except auth_errors.UserIsBroken:
		raise error_responses.user_is_broken

	except upload_errors.FileIsntImage:
		raise error_responses.file_isnt_image

	except upload_errors.FileSizeBiggerThan:
		raise error_responses.filesize_bigger_than

	except Exception as exp:
		print(exp)
		raise error_responses.server_internal