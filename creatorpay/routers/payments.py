from fastapi import APIRouter

router = APIRouter(
    prefix="/payments",
    tags=["payments"],
)
