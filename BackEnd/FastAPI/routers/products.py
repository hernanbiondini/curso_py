from fastapi import APIRouter

router = APIRouter()

products_list = ["PC","Mesa","Televisor","Heladera"]

@router.get("/products")
async def users():
    return products_list