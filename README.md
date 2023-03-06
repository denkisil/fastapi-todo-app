# this is todo app, builded with FastAPI, SQLite, Peewee

# Requirements: Python 3.10+

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

3. Create `todos.db` file in project's root folder

4. Before you run server uncomment 10 line in `src/app.py` file

5. Then run:
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
	description: str
	important: bool = False
```

TodoUpdate:
```
	title: str | None = None
	description: str | None = None
	important: bool | None = None
	complete: bool | None = None
```

TODO:
- make client on Vue
