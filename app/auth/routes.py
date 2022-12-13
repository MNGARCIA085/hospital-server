from fastapi import APIRouter,Depends,HTTPException,Query
from sqlalchemy.orm import Session
from database.configuration import get_db
from . import models
from . import schemas
from . import crud
import functools


router = APIRouter(
    prefix="/auth",
    responses={404: {"description": "Not found"}},
)



""" 1. USERS """

# post a new user
@router.post("/users/",status_code=201) #, response_model=schemas.User
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    crud.post_user(user=user,db=db)


# get user
@router.get("/users/",response_model=list[schemas.UserOut])
def read_users(
                skip: int = 0, 
                limit: int = 100, 
                db: Session = Depends(get_db),
                name: str | None = None,
                last_name: str | None = None,
            ):
        return crud.get_users(
                skip=skip,
                limit=limit,
                last_name=last_name,
                name=name,
                db=db
            )


# get user by id
@router.get("/users/{user_id}",response_model=schemas.UserOut) #,
def read_user(user_id,db: Session = Depends(get_db)):
    return crud.get_user_by_id(user_id,db)


# Update an user
@router.put('/users/{user_id}',response_model=schemas.UserOut,status_code=201)
def update_user(user_id: int,user: schemas.User, db: Session = Depends(get_db)):
    return crud.update_user(user_id,user,db)


# Delete an user
@router.delete("/users/{user_id}") #, response_model=schemas.User
def delete_user(user_id,db: Session = Depends(get_db)):
    return crud.delete_user(user_id,db)



""" 2. GROUPS """


# create a new group
@router.post("/groups/",status_code=201) #, response_model=schemas.User
def create_group(group: schemas.Groups, db: Session = Depends(get_db)):
    return crud.post_group(group,db)


# list of all groups
@router.get("/groups/",response_model=list[schemas.GroupsOut])
def read_groups(
            skip: int = 0, 
            limit: int = 100, 
            db: Session = Depends(get_db),
        ):
        return crud.get_groups(skip,limit,db)





# get group by id
@router.get("/groups/{group_id}",response_model=schemas.GroupsOut) #,
def read_user(group_id,db: Session = Depends(get_db)):
    return crud.get_group_by_id(group_id,db)



# Delete a group
@router.delete("/groups/{group_id}") #, response_model=schemas.User
def delete_user(group_id,db: Session = Depends(get_db)):
    return crud.delete_user(group_id,db)







""" 3. GROUPS AND USERS """



""" User and groups """
@router.post("/groupsUser/")
def create_usergroups(u: int, g: int, db: Session = Depends(get_db)):
    db_item = models.UserGroups(user_id=u,group_id=g)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item




# agregar usuario y grupos a los que pertenece (le paso un usuario y el id de los grupos)
@router.post("/userAndGroups/",status_code=201)
def create_user_and_groups(
                        user: schemas.User, 
                        groups: list[int], 
                        db: Session = Depends(get_db)):
    return crud.create_user_and_assign(user,groups,db)




# delete groups per user
@router.delete("/userAndGroups/")
def delete_groups_per_user(
                        user_id: int, 
                        groups: list[int], 
                        db: Session = Depends(get_db)):
    return crud.delete_groups_per_user(user_id,groups,db)



#https://dassum.medium.com/building-rest-apis-using-fastapi-sqlalchemy-uvicorn-8a163ccf3aa1


#https://hackersandslackers.com/database-queries-sqlalchemy-orm/