# this is todo app, builded with FastAPI, Supabase, Passlib

### Requirements: 
	- Python 3.11+

# Deploy

1. Clone repository
```
git clone https://github.com/denkisil/fastapi-todo-app
```

2. Install requirements
```
pip install -r requirements.txt
```
or
```
pipenv install -r requirements.txt
```

3. Add environment variables (see in .env.example)

4. Then run:
```
python main.py
```
or
```
pipenv run main.py
```

5. go to `127.0.0.1:8000/docs` for testing APi


# API

#### GET
	-	`/api/todos` - all todos. Auth required

	-	`/api/todos/{id}` - todo by id. Auth required


#### POST 
	-	`/api/todos/new` - create new todo. Request model - TodoCreate. Auth required

	-	`/api/users/new` - create new user. Request model - UserCreate

	-	`/api/users/auth` - get auth token. Request model - UserAuth

#### PUT 
	-	`/api/todos/{id}` - update todo by id. Request model - TodoUpdate. Auth required

#### DELETE 
	-	`/api/todos/{id}` - delete todo by id. Auth required

	-	`/api/users/user_delete` - delete your account with created todos. Auth required



# Models

TodoCreate:
```
	title: str
	desc: str
	important: bool = False
```

TodoUpdate:
```
	title: str | None = None
	desc: str | None = None
	important: bool | None = None
	complete: bool | None = None
```

UserCreate:
```
	username: str = Field(min_length=6, max_length=32)
	password: str = Field(min_length=8, max_length=32)
```

UserAuth:
```
	username: str
	password: str
```