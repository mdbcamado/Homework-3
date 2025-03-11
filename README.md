# MLflow-FastAPI-Docker Project

## Overview
This project integrates **FastAPI**, **MLflow**, and **Docker** to create a scalable machine learning workflow. It allows users to:
- Upload new training data
- Retrain and update the ML model
- Track model performance using **MLflow**
- Deploy the FastAPI service in a containerized environment

## Features
- **FastAPI Backend:** Serves ML predictions and handles retraining requests.
- **MLflow Integration:** Tracks model versions, training metrics, and artifacts.
- **Docker Support:** Ensures reproducibility and easy deployment.
- **Jinja2 UI:** Simple web interface for user interactions.
- **Dagster Workflow:** Orchestrates data preprocessing and model training.

---

## Setup Instructions
### Prerequisites
Ensure you have the following installed:
- [Docker](https://docs.docker.com/get-docker/)
- [Python 3.8+](https://www.python.org/downloads/)
- [MLflow](https://mlflow.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)
- [Dagster](https://dagster.io/)

### Clone the Repository
```sh
git clone https://github.com/your-username/mlflow-fastapi-docker.git
cd mlflow-fastapi-docker
```

### Install Dependencies
Using `pip`:
```sh
pip install -r requirements.txt
```

---

## Running the FastAPI Application
### Option 1: Run Locally
Start the FastAPI app with:
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Option 2: Run with Docker
Build and run the Docker container:
```sh
docker build -t mlflow-fastapi .
docker run -p 8000:8000 mlflow-fastapi
```

---

## MLflow Tracking
To start the MLflow UI for tracking models:
```sh
mlflow ui --host 0.0.0.0 --port 5000
```
Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) to monitor experiments.

---
