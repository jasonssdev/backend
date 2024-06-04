from fastapi import APIRouter

router = APIRouter(prefix="/products",
                    tags=["products"],
                    responses={404: {"message":"Not found"}})

product_list = ["product_1", "product_2", "product_3", "product_4", "product_5"]

@router.get("/")
async def products():
    return product_list

@router.get("/{id}")
async def products(id: int):
    return product_list[id]