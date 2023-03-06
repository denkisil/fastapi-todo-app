from src.routes import todos_route

from fastapi import APIRouter

router = APIRouter(prefix="/api")

router.include_router(todos_route.router)