from fastapi import FastAPI
from pydantic import BaseModel  # pylint: disable=no-name-in-module


app = FastAPI()


class Item(BaseModel):
    message: str


@app.get("/")
async def root():
    return {"message": "API is Working!"}


@app.post("/echo")
async def echo(item: Item):
    return {"echo": item.message}
