from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
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



@app.get("/users")
async def users():
    return users_list

# Path
@app.get("/user/{id}")
async def users(id:int):
     return search_user(id)
# Query
@app.get("/user/")
async def users(id:int):
     return search_user(id)

def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        error = "No se ha encontrado el usuario con id {}"
        return {"error":error.format(id)}

@app.post("/user/")
async def users(user:User):
    if type(search_user(user.id)) == User:
        error = "El usuario con id {} ya existe"
        return {"error":error.format(user.id)}
    else:
        users_list.append(user)

