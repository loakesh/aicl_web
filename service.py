
from fastapi import FastAPI,Request
from typing import Optional
from pydantic import BaseModel

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class User(BaseModel):
    id: int
    name = 'Loke'
    signup: Optional[bool] = None
    list1: Optional[list] = []

class STU(BaseModel):
    name: str
    mark: int
    age: int

@app.get("/")
def home():
    return {"Hey": "Wassup"}

@app.get("/movie/{star}")
def imdb(star: str, rating: int, review: Optional[str] = "GOOD"):
    return {"star": star, "rating": rating ,"review": review}

@app.put("/endpoint")
async def endpoint(User: User):
    return {"name": User.name , "signup": User.signup , "list1": User.list1 }

@app.post("/mypostendpoint")
async def endpoint2(User: STU):
    return {"name": User.name , "mark": User.mark , "age": User.age }

@app.get("/security")
async def sec(token:str):
    authToken = "Y3Jpc3RpYW5vcm9uYWxkbw=="
    if token !="" or token==authToken:
        authorisation = "success"
    else:
        authorisation = "failed"
    
    return{"server_pass":authorisation}


@app.get("/web", response_class=HTMLResponse)
async def web():
   code = """
        <html>
        <head>
        <title>Some HTML in here</title>
        </head>
        <body>
        <h1>Look ma! HTML!</h1>
        </body>
        </html>

    """
   return code


class user1(BaseModel):
    name:str
    password:str
    email:str


@app.get("/login", response_class=HTMLResponse)
async def webpage(request:Request):
    return templates.TemplateResponse('index.html', context={'request':request})


@app.post("/create_user")
async def create_user(user:user1):

    db = eval(open("db.json","r").read())

    user_profile = {"name":user.name,
                    "password":user.password,
                    "email":user.email}


    db["users"].append(user_profile)
    open("db.json","w+").write(str(db))
    return {"status":"success"}

class users(BaseModel):
    name:str
    password:str

@app.post("/login_user")
async def create_user(user:users):
 
    userdb = eval(open("db.json","r").read())  
    for each in  userdb["users"]:
        if each["name"]==user.name and each["password"]==user.password:
            return {"status":"Success"}
        else:
            pass
    return {"status":"Wrong password or Username"}