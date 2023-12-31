from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# Para correrlo posicionarse en el drectorio del archivo y ejecutar
# py -m uvicorn basic_auth_users:app --reload

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

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
        "password": "123456"
    },
    "victor": {
        "username": "victor", 
        "full_name": "Victor Biondini", 
        "email": "user1@example.com", 
        "disabled": True,
        "password": "abc"
    }
}

def search_user_db(username:str):
    if username in users_db:
        return UserDB(**users_db[username])


def search_user(username:str):
    if username in users_db:
        return User(**users_db[username])
async def current_user(token:str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Credenciales de autenticacion inválidas",
            headers={"WWW-Authenticate": "Bearer"})
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Usuario inactivo",
            headers={"WWW-Authenticate": "Bearer"})
    return user

@router.post("/login2")
async def login(form:OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="El usuario no es correcto")
    user =  search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail="La contraseña no es la correcta")
    return {"access_token": user.username, "token_type":"bearer"}

@router.get("/users/me2")
async def me(user:User = Depends(current_user)):
    return user