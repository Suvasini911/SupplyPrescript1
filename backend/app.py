from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3
import pandas as pd
import joblib

from optimizer import get_recommendations

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and encoders
model = joblib.load("model.pkl")
encoders = joblib.load("encoder.pkl")


class Shipment(BaseModel):
    scheduled_days: int
    benefit_per_order: float
    sales_per_customer: float
    category_id: int
    quantity: int
    product_price: float
    shipping_mode: str
    market: str
    order_region: str


@app.get("/")
def home():
    return {"message": "SupplyPrescript API Running"}


@app.post("/predict")
def predict(data: Shipment):

    shipping_mode = encoders["Shipping Mode"].transform(
        [data.shipping_mode]
    )[0]

    market = encoders["Market"].transform(
        [data.market]
    )[0]

    order_region = encoders["Order Region"].transform(
        [data.order_region]
    )[0]

    sample = pd.DataFrame([{
        "Days for shipment (scheduled)": data.scheduled_days,
        "Benefit per order": data.benefit_per_order,
        "Sales per customer": data.sales_per_customer,
        "Category Id": data.category_id,
        "Order Item Quantity": data.quantity,
        "Product Price": data.product_price,
        "Shipping Mode": shipping_mode,
        "Market": market,
        "Order Region": order_region
    }])

    prediction = int(model.predict(sample)[0])

    recommendations = get_recommendations(prediction)

    return {
        "prediction": prediction,
        "prediction_text":
            "High Delay Risk" if prediction == 1 else "Low Delay Risk",
        "recommendations": recommendations
    }

@app.post("/save-decision")
def save_decision(data: dict):

    conn = sqlite3.connect("supplyprescript.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO decisions
        (shipment_id, prediction, action)
        VALUES (?, ?, ?)
    """,(
        data["shipment_id"],
        data["prediction"],
        data["action"]
    ))

    conn.commit()
    conn.close()

    return {"message":"Decision Saved Successfully ✅"}

@app.get("/history")
def history():

    conn = sqlite3.connect("supplyprescript.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM decisions")

    rows = cursor.fetchall()

    conn.close()

    return rows


    # FastAPI application initialization

# Load trained ML model

# Prediction endpoint

# Save decision endpoint