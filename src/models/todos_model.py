from pydantic import BaseModel

class TodoCreate(BaseModel):
	title: str
	description: str
	important: bool = False

	class Config:
		schema_extra = {
			'example': {
				'title': 'Take a cup of tea',
				'description': 'Take a cup of tea with tasty sandwichies',
				'important': True
			}
		}


class TodoUpdate(BaseModel):
	title: str | None = None
	description: str | None = None
	important: bool | None = None
	complete: bool | None = None

	class Config:
		schema_extra = {
			'example': {
				'title': 'Take a cup of tea',
				'description': 'Take a cup of tea with tasty sandwichies',
				'important': True,
				'complete': True
			}
		}