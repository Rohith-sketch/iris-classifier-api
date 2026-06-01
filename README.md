# 🌸 Iris Classifier API

This is a production-ready Machine Learning API built with FastAPI. It predicts the species of an Iris flower based on its petal and sepal measurements.

## Features
* **FastAPI** web server
* **Pydantic** data validation
* **Scikit-Learn** ML model loaded on lifespan startup
* **Pytest** automated testing
* **Docker** containerized

## How to Run (Using Docker)
1. Build the image: `docker build -t iris-api:dev .`
2. Run the container: `docker run -p 8000:8000 iris-api:dev`
3. View the docs at `http://localhost:8000/docs`

## Example Request
You can test the API using this curl command in your terminal:
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2}'