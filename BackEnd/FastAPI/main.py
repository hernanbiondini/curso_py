# Git proyecto https://github.com/mouredev/Hello-Python/tree/main/Backend
# Documentación oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"
# Para correrlo posicionarse en el drectorio del archivo y ejecutar: py -m uvicorn main:app --reload
# instalar pymongo: py -m pip install "pymongo"  
# Url local: http://127.0.0.1:8000/url
# Detener el server: CTRL+C
# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc

from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return "Hola FastAPI"

