from fastapi import FastAPI
from pydantic import BaseModel  # pylint: disable=no-name-in-module


app = FastAPI()


class Item(BaseModel):
    """Item model."""

    message: str


@app.get("/")
async def root():
    """Root route."""
    return {"message": "API is Working!"}


@app.post("/echo")
async def echo(item: Item):
    """Echo route."""
    return {"echo": item.message}
