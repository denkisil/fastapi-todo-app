from src.database.todos import Todos
from src.routes import main_route

from fastapi import FastAPI 


app = FastAPI()


app.include_router(main_route.router)