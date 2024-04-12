from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

name = "sujin"

@app.get("/")
def read_root():
    print(name)
    return 0

@app.post("/")
def create_root():
    return 0

@app.put("/")
def update_root():
    name = input("type name")
    return 0

@app.delete("/")
def delete_root():
    name = "empty"
    return 0