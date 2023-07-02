from fastapi import FastAPI

app = FastAPI()


#@app.get("/")
#async def root():
#    return {"message": "Hello World"}

@app.get("/")
async def root():
    return "Hola FastAPI"

@app.get("/saludo")
async def root():
    return {"saludo":"hola"}