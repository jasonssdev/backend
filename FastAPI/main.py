from fastapi import FastAPI
from routers import products
from routers import users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers

app.include_router(products.router)
app.include_router(users.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return "Hi FastAPI"

@app.get("/url")
async def url():
    return {"url": "https://mouredev.com/python"}

# server start -> uvicorn main:app --reload
# server stop -> CTRL+C

# Swager docs: http://127.0.0.1:8000/docs
# Redocly docs: http://127.0.0.1:8000/redoc

# GET - Obtain data