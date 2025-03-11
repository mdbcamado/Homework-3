from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi import Request
import numpy as np
import pandas as pd  
import joblib


MODEL_PATH = "models/model.joblib"
SCALER_PATH = "models/scaler.joblib"
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

app = FastAPI()


templates = Jinja2Templates(directory="src/templates")


class PredictionInput(BaseModel):
    mass: float
    width: float
    height: float
    color_score: float

@app.get("/")
def read_root(request: Request):
    """Serve the prediction form as a separate page."""
    return templates.TemplateResponse("prediction_form.html", {"request": request})

@app.post("/predict/")
def predict(request: Request, mass: float = Form(...), width: float = Form(...), height: float = Form(...), color_score: float = Form(...)):
    """Receives structured input and returns a prediction."""
    
    numerical_features = ['mass', 'width', 'height', 'color_score']  
    features = pd.DataFrame([[mass, width, height, color_score]], columns=numerical_features) 
    
  
    features_scaled = scaler.transform(features)  

   
    features_scaled_df = pd.DataFrame(features_scaled, columns=numerical_features)


    prediction = model.predict(features_scaled_df)
    probabilities = model.predict_proba(features_scaled_df)

    label_map = {1: "apple", 2: "mandarin", 3: "orange", 4: "lemon"}

    return templates.TemplateResponse("prediction_result.html", {
        "request": request, 
        "prediction": label_map[prediction[0]],
        "probabilities": probabilities.tolist()
    })
