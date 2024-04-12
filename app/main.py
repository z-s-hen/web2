from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

name = "sujin"

@app.get("/")
def read_root():
    #print(name)
    return {"name" : name}

@app.post("/")
#def create_item(item: Item):
#    return item
def create_root(new_name: Item):
    return {"updated" : new_name}

@app.put("/")
def update_root(upd_name: Item):
    if name != upd_name:
        name = upd_name
    return {"edited" : name}
#def update_root():
#    return 0

@app.delete("/")
def delete_root():
    name = 0
    return {"deleted"}