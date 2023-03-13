from src.database.todos import Todos
from src.routes import main_route

from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI

app = FastAPI()


app.mount('/imgs', StaticFiles(directory='imgs'), name='images')


app.include_router(main_route.router)