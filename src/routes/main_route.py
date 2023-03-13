from src.routes import todos_route, user_route, images_route

from fastapi import APIRouter


router = APIRouter(prefix="/api")


router.include_router(todos_route.router)

router.include_router(user_route.router)

router.include_router(images_route.router)