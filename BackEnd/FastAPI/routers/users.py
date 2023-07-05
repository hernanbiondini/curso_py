from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/users",
                   tags=["users"])
# py -m uvicorn users:app --reload 

class User(BaseModel):
    id:int
    name: str
    surname: str
    url:str
    age:int

users_list = [
    User(id=1,name="John", surname="Doe", url="https://example.com/johndoe", age=25),
    User(id=2,name="Jane", surname="Smith", url="https://example.com/janesmith", age=30),
    User(id=3,name="Michael", surname="Johnson", url="https://example.com/michaeljohnson", age=40),
    User(id=4, name="Emily", surname="Brown", url="https://example.com/emilybrown", age=35)
]



@router.get("/")
async def users():
    return users_list

# Path
@router.get("/{id}")
async def users(id:int):
     return search_user(id)
# Query
@router.get("/")
async def users(id:int):
     return search_user(id)

@router.post("/", response_model=User, status_code=201)
async def users(user:User):
    if type(search_user(user.id)) == User:
        error = "El usuario con id {} ya existe"
        raise HTTPException(status_code=409, detail=error.format(user.id))
        #error = "El usuario con id {} ya existe"
        #return {"error":error.format(user.id)}
    users_list.append(user)
    return user

@router.put("/user/")
async def users(user:User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] == user
            found = True
    if not found:
        error = "No se ha encontrado el usuario con id {}"
        return {"error":error.format(user.id)}
    return user

@router.delete("/user/{id}")
async def users(id:int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        error = "No se ha encontrado el usuario con id {}"
        return {"error":error.format(id)}
    return id

def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        error = "No se ha encontrado el usuario con id {}"
        return {"error":error.format(id)}