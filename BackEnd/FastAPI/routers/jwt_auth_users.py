from fastapi import APIRouter, Depends, HTTPException, status
#from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

# Para correrlo posicionarse en el drectorio del archivo y ejecutar
# py -m uvicorn jwt_auth_users:app --reload

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "02df45a1b7c8e790d36fe2a9c4bc3e1f38482d647b103e5af6be8923f570437c"


router = APIRouter()
#app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])



class User(BaseModel):
    username: str
    full_name: str
    email:str
    disabled:bool

class UserDB(User):
    password: str

users_db = {
    "hernan": {
        "username": "hernan", 
        "full_name": "Hernan Biondini", 
        "email": "user1@example.com", 
        "disabled": False,
        "password": "$2a$12$uKs/akCjkz6ySVwXoWBiBOJSKb4LWaSYKzsWlmlYKvEH5lE4ZxwTe" # 123456
    },
    "victor": {
        "username": "victor", 
        "full_name": "Victor Biondini", 
        "email": "user1@example.com", 
        "disabled": True,
        "password": "$2a$12$uKs/akCjkz6ySVwXoWBiBOJSKb4LWaSYKzsWlmlYKvEH5lE4ZxwTe" # 123456
    }
}

def search_user_db(username:str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username:str):
    if username in users_db:
        return User(**users_db[username])

async def auth_user(token:str = Depends(oauth2)):
    exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Credenciales de autenticacion inválidas",
            headers={"WWW-Authenticate": "Bearer"})
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception

    except JWTError:
        raise exception
    return search_user(username) 

async def current_user(user:User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Usuario inactivo",
            headers={"WWW-Authenticate": "Bearer"})
    return user
    
#@app.post("/login")
@router.post("/login")
async def login(form:OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="El usuario no es correcto")
    user =  search_user_db(form.username)

    

    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=400, detail="La contraseña no es la correcta")
    
    access_token = {"sub": user.username,
                    "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}



    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type":"bearer"}

#@app.get("/users/me")
@router.get("/users/me")
async def me(user:User = Depends(current_user)):
    return user