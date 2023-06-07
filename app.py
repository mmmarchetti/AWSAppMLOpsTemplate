from fastapi import FastAPI
from pydantic import BaseModel  # pylint: disable=no-name-in-module
from src.models.train_model import train_model
from src.models.predict_model import predict_model


app = FastAPI()


# Define data models
class IrisFeatures(BaseModel):
    """Iris features model."""

    features: list


class IrisPrediction(BaseModel):
    """Iris prediction model."""

    prediction: int


class Item(BaseModel):
    """Item model."""

    message: str


@app.post("/train", response_model=IrisPrediction)
async def train():
    """Train route."""
    score = train_model()
    return {"prediction": score}


@app.post("/predict", response_model=IrisPrediction)
async def predict(iris: IrisFeatures):
    """Predict route."""
    prediction = predict_model(iris.features)
    return {"prediction": prediction[0]}


@app.get("/")
async def root():
    """Root route."""
    return {"message": "API is Working!"}


@app.post("/echo")
async def echo(item: Item):
    """Echo route."""
    return {"echo": item.message}
