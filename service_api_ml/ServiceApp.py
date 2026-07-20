"""
Простое API
pip install fastapi uvicorn pydantic scikit-learn pandas
Start App-> ServiceApp.py: python ServiceApp.py

Check API
curl -X GET http://127.0.0.1:5000/health
curl -X GET http://127.0.0.1:5000/stats
curl -X POST http://127.0.0.1:5000/predict_model -H "Content-Type: application/json" -d "{\"Pclass\":3, \"Age\": 22.0, \"Fare\":7.2500}"
"""

from fastapi import FastAPI, Request, HTTPException
import pickle
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

request_count = 0

class PredictionInput(BaseModel):
    Pclass: int
    Age: float
    Fare: float

@app.get("/stats")
def stats():
    return {"request_count": request_count}

@app.get("/health")
def health():
    return {"status": "OK"}

@app.post("/predict_model")
def predict_model(input_data: PredictionInput):
    global request_count
    request_count += 1
    # Создание DataFrame из данных

    new_data = pd.DataFrame({
        'Pclass': [input_data.Pclass],
        'Age': [input_data.Age],
        'Fare': [input_data.Fare]
    })

    # Предсказание
    predictions = model.predict(new_data)

    # Преобразование результата в человеко-читаемый формат
    result = "Survived" if predictions[0] == 1 else "Not Survived"

    return {"prediction": result}

if __name__ == '__main__':
    import uvicorn
    #uvicorn.run(app, host="127.0.0.1", port=5000)
    uvicorn.run(app, host="0.0.0.0", port=5000)


# SWAGGER UI
# http://127.0.0.1:5000/docs














































