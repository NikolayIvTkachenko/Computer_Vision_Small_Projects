from fastapi import FastAPI, Request, HTTPException
import pickle
import pandas as pd
from pydantic import BaseModel

import requests

def predict_model(data):
    url = 'http://127.0.0.1:5000/predict_model'

    response = requests.post(url, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error":f"Request failed with status code {response.status_code}"}
# Пример данных для предсказания
data = {
    "Pclass": 1,
    "Age": 22.0,
    "Fare": 150.250
}

prediction = predict_model(data)
print(prediction)