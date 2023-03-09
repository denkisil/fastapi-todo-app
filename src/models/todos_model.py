from pydantic import BaseModel, Field

class TodoCreate(BaseModel):
	title: str = Field(min_length=6, max_length=32)
	desc: str = Field(min_length=8, max_length=128)
	important: bool = Field(default=False)

	class Config:
		schema_extra = {
			'example': {
				'title': 'Take a cup of tea',
				'desc': 'Take a cup of tea with tasty sandwichies',
				'important': True
			}
		}


class TodoUpdate(BaseModel):
	title: str | None = Field(default=None, min_length=6, max_length=32)
	desc: str | None = Field(default=None, min_length=8, max_length=128)
	important: bool | None = Field(default=None)
	complete: bool | None = Field(default=None)

	class Config:
		schema_extra = {
			'example': {
				'title': 'Take a cup of tea',
				'desc': 'Take a cup of tea with tasty sandwichies',
				'important': True,
				'complete': True
			}
		}