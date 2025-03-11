import uvicorn
import pandas as pd
from src.data.load_data import load_raw_data
from src.data.preprocess import preprocess_data
from src.models.train_model import train_model
from src.models.evaluate_model import evaluate_model

def start_fastapi():
    """Starts the FastAPI server."""
    print("Starting FastAPI server...")
    uvicorn.run("src.models.predict:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
 
    start_fastapi()
