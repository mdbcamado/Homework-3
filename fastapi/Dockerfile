FROM python:3.10

WORKDIR /app

# Copy the requirements file into the container
COPY ../requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the source code
COPY ../src /app/src


# Run FastAPI
CMD ["uvicorn", "src.models.predict:app", "--host", "0.0.0.0", "--port", "8000"]
