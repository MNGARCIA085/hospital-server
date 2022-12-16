from fastapi import APIRouter,Depends,HTTPException,Query
from sqlalchemy.orm import Session
from database.configuration import get_db
from . import models
from .doctors import routes as doc_routes
import functools


router = APIRouter(
    prefix="/staff",
    responses={404: {"description": "Not found"}},
)



router.include_router(doc_routes.router,tags=['doctors'])


