from pydantic import BaseModel, Field

class UserBase(BaseModel):
	username: str = Field(min_length=6, max_length=32)


class UserCreate(UserBase):
	password: str = Field(min_length=8, max_length=32)


	class Config:
		schema_extra = {
			'example': {
				'username': 'Stuart',
				'password': '123456789'
			}
		}


class UserAuth(UserCreate):
	pass
	

class UserUpdate(BaseModel):
	name: str | None = Field(default=None, min_length=6, max_length=32)


	class Config:
		schema_extra = {
			'example': {
				'username': 'Benjamin'
			}
		}



