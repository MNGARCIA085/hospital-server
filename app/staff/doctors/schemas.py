from pydantic import BaseModel
from typing import List, Union, Optional
from auth.schemas import User




class Child(BaseModel):
    descripcion:str

    class Config:
        orm_mode = True




class Doctor(BaseModel):
    #user: User
    user_id:int

    class Config:
        orm_mode = True


class Especialidad(BaseModel):
    descripcion: str

    class Config:
        orm_mode = True


# response models
class DoctorOut(BaseModel):
    id:int
    user:Optional[User]



    class Config:
        orm_mode = True






class EspecialidadOut(Especialidad):
    id:int
    doctor: List[Doctor]

    class Config:
        orm_mode = True