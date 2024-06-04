from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
                    prefix="/user",
                    tags=["user"],
                    responses={404: {"message":"Not found"}}
                )

# server start -> uvicorn users:app --reload

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1, name="Jason", surname="Dev", url="https://jasonssdev.com", age=33),
            User(id=2, name="Brais", surname="Dev", url="https://moure.dev", age=34),
            User(id=3, name="Brais", surname="Moure", url="https://mouredev.com", age=35)]


    
@router.get("/")
async def usersjson():
    return users_list

#path
@router.get("/{id}")
async def user(id: int):
    return search_user(id)

@router.post("/", status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="user already created")
    else:
        users_list.append(user)
        return user

@router.put("/", status_code=200)
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        raise HTTPException(status_code=404, detail="user not updated")
    else:
        return user
    
@router.delete("/{id}", status_code=200)
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        raise HTTPException(status_code=404, detail="user not deleted")
    else:
        return user


#function
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"user not found"}