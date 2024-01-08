from fastapi import APIRouter

from src.api.v1.endpoints import test

api_router = APIRouter()
api_router.include_router(test.router, tags=["test"])
