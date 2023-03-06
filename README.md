# this is todo app, builded with FastAPI, SQLite, Peewee

### API

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
