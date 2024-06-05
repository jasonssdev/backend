from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool

class UserDB(BaseModel):
    password: str

users_db = {
    "mouredev":{
        "username": "mouredev",
        "fullname": "Brais Moure",
        "email": "braismoure@mouredev.com",
        "disabled": False,
        "password": "123456"
    },
    "mouredevs":{
        "username": "mouredev2",
        "fullname": "Brais Moure 2",
        "email": "braismoure2@mouredev.com",
        "disabled": True,
        "password": "654321"
    },
}

#function
def search_user(username: str):
    if username in users_db:
        return UserDB(users_db[username])
    
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="Incorret user")
    user = search_user(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail="Incorret password")
    return {"access_token":"user.username", "token_type":"bearer"}