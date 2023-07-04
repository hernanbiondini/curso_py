from fastapi import FastAPI

app = FastAPI()
from routers import products, users

# Routers
app.include_router(products.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return "Hola FastAPI"
