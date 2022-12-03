from fastapi import APIRouter,Depends,HTTPException,Query
from sqlalchemy.orm import Session
from database.configuration import get_db
from . import models
from . import schemas
import functools


router = APIRouter(
    prefix="/auth",
    responses={404: {"description": "Not found"}},
)




""" USERS """

@router.post("/users/",status_code=201) #, response_model=schemas.User
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    db_item = models.User(**user.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item




#iterable para buscar





@router.get("/users/",response_model=list[schemas.UserOut])
def read_users(
                skip: int = 0, 
                limit: int = 100, 
                db: Session = Depends(get_db),
                q: str | None = None,
                name: list[str] | None = Query(default=None)
            ):
        # filtrado
        aux = models.User.id
        queries = [aux >= 0]
        if name: # lista
            queries_name = []
            for n in name:
                aux = models.User.name
                q = aux==n
                queries_name.append(q)
            query_name = functools.reduce(lambda a,b: a|b,queries_name)
            queries.append(query_name)
        query = functools.reduce(lambda a,b: (a&b),queries)
        # respuesta
        return list(db.query(models.User).filter(query).offset(skip).limit(limit))
        #return db.query(models.User).offset(skip).limit(limit).all()




@router.get("/users/{user_id}",response_model=schemas.UserOut) #,
def read_user(user_id,db: Session = Depends(get_db)):
    return db.query(models.User).filter(models.User.id==user_id).first()



# Update an user
@router.put('/users/{user_id}',response_model=schemas.UserOut,status_code=201)
def update_user(user_id: int,user: schemas.User, db: Session = Depends(get_db)):
    """
    Update an Item stored in the database
    """

    """
    hero_data = hero.dict(exclude_unset=True)
        for key, value in hero_data.items():
            setattr(db_hero, key, value)
    """
    db_user = db.query(models.User).filter(models.User.id==user_id).first()
    if db_user:
        db_user.name = user.name
        db.commit()
        db.refresh(db_user)
        return db_user
    else:
        raise HTTPException(status_code=400, detail="Item not found with the given ID")





@router.delete("/users/{user_id}") #, response_model=schemas.User
def delete_user(user_id,db: Session = Depends(get_db)):
    db.query(models.User).filter_by(id=user_id).delete()
    db.commit()
    return {'Mensaje':'Registro eliminado'}









""" Groups """
@router.post("/groups/",status_code=201) #, response_model=schemas.User
def create_group(group: schemas.Groups, db: Session = Depends(get_db)):
    db_item = models.Groups(**group.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item



@router.get("/groups/",response_model=list[schemas.GroupsOut])
def read_departments(
        skip: int = 0, 
        limit: int = 100, 
        db: Session = Depends(get_db),
        q: str | None = None):
        if q:
                aux = db.query(models.Groups).filter(models.Groups.id == q).offset(skip).limit(limit)
                return list(aux)     
        return db.query(models.Groups).offset(skip).limit(limit).all()





""" Groups and Users """
@router.post("/groupsUser/")
def create_usergroups(u: int, g: int, db: Session = Depends(get_db)):
    db_item = models.UserGroups(user_id=u,group_id=g)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item




#https://dassum.medium.com/building-rest-apis-using-fastapi-sqlalchemy-uvicorn-8a163ccf3aa1


#https://hackersandslackers.com/database-queries-sqlalchemy-orm/