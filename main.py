from fastapi import FastAPI
from fastapi.responses import FileResponse


app = FastAPI()


@app.get("/")
def main():
    return FileResponse("index.html")


@app.get("/home")
def home():
    return FileResponse("home.html")


@app.get("/friends")
def friends():
    return FileResponse("friends.html")