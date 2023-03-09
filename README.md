# this is todo app, builded with FastAPI, SQLite, Supabase

# Requirements: Python 3.11+

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

# API

#### GET `/api/todos` - all todos

#### GET `/api/todos/{id}` - todo by id

#### POST `/todos/new` - create new todo. Request model - TodoCreate

#### PUT `/todos/{id}` - update todo by id. Request model - TodoUpdate

#### DELETE `/api/todos/id` - delete todo by id

### Models

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

Todo:
[ ] Create simple client
[ ] Add simple Authentication
