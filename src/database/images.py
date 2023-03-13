from src.database.database import Base

from fastapi import UploadFile, File
import shutil
import os

class Images(Base):


	def __init__(self):
		super().__init__()


	def upload_image(self, filename: str, file: bytes, user: dict):

		filepath = os.path.join(os.getcwd(), 'imgs', filename)

		with open(filepath, 'wb') as f:
			f.write(file)


		image_obj = {
			'filename': filename,
			'filepath': '/imgs/' + filename, 
			'user_id': user['id']
		}

		image_uploaded = self.db.table('images').insert(image_obj).execute()

		return image_uploaded


		


