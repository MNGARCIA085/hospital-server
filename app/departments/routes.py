from fastapi import APIRouter,Depends,HTTPException,Query
from sqlalchemy.orm import Session
from database.configuration import get_db
from . import models
from . import schemas
import functools


router = APIRouter(
    prefix="/departments",
    responses={404: {"description": "Not found"}},
)



""" SEDES """

@router.post("/locations/",status_code=201) #, response_model=schemas.User
def create_department(sede: schemas.Sede, db: Session = Depends(get_db)):
    db_item = models.Sede(**sede.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item





@router.get("/locations/",response_model=list[schemas.SedeOut])
def read_departments(
                skip: int = 0, 
                limit: int = 100, 
                db: Session = Depends(get_db)
            ):
        # filtrado
        return db.query(models.Sede).offset(skip).limit(limit).all()


