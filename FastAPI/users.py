from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# server start -> uvicorn users:app --reload

# json list
my_json_list = [{"name":"Jason", "surname":"Dev", "url":"https://jasonssdev.com", "age":33},
                {"name":"Brais", "surname":"Dev", "url":"https://moure.dev", "age":34},
                {"name":"Brais", "surname":"Moure", "url":"https://mouredev.com", "age":35}]

@app.get("/usersjson")
async def usersjson():
    return my_json_list

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1, name="Jason", surname="Dev", url="https://jasonssdev.com", age=33),
            User(id=2, name="Brais", surname="Dev", url="https://moure.dev", age=34),
            User(id=3, name="Brais", surname="Moure", url="https://mouredev.com", age=35)]


    
@app.get("/users")
async def usersjson():
    return users_list

#path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)
#query
@app.get("/userquery/")
async def user(id: int):
    return search_user(id)

@app.post("/user/")
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"error":"user already created"}
    else:
        users_list.append(user)
        return user

@app.put("/user/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error":"user not updated"}
    else:
        return user
    
@app.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error":"user not deleted"}
    else:
        return user


#function
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"user not found"}