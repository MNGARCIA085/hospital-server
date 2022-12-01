from pydantic import BaseModel
from typing import List, Union



class User(BaseModel):
    #id: int
    name: str

    class Config:
        orm_mode = True


class Groups(BaseModel):
    #id: int
    name: str

    class Config:
        orm_mode = True


# response models
class UserOut(User):
    id:int
    groups: List[Groups]


class GroupsOut(Groups):
    id:int
    users: List[User]
