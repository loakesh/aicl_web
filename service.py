from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name = 'Loke'
    signup: Optional[bool] = None
    list1: Optional[list] = []

@app.get("/")
def home():
    return {"Hey": "Wassup"}

@app.get("/movie/{star}")
def imdb(star: str, rating: int, review: Optional[str] = "GOOD"):
    return {"star": star, "rating": rating ,"review": review}

@app.put("/endpoint")
def endpoint(User: User):
    return {"name": User.name , "signup": User.signup , "list1": User.list1 }

