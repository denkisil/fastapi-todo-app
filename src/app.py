from src.database.database import db, Todos
from src.routes import main_route

from fastapi import FastAPI 

app = FastAPI()

try:
	db.connect()
	db.create_tables([Todos])
except(e):
	raise e


app.include_router(main_route.router)
