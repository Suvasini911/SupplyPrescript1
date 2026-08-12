import sqlite3
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier


DB_NAME = "supplyprescript.db"
DATASET_PATH = "../dataset/supply_chain_data.csv"

MODEL_PATH = "model.pkl"
ENCODER_PATH = "encoder.pkl"


def check_discrepancy(decision_id):
    """
    Check the difference between predicted
    and actual cost for an evaluated decision.
    """

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            predicted_cost,
            actual_cost,
            cost_difference,
            outcome
        FROM decisions
        WHERE id = ?
    """, (decision_id,))

    result = cursor.fetchone()

    conn.close()

    if result is None:
        return {
            "should_retrain": False,
            "message": "Decision not found"
        }

    predicted_cost, actual_cost, cost_difference, outcome = result

    if predicted_cost is None or actual_cost is None:
        return {
            "should_retrain": False,
            "message": "Decision has not been evaluated yet"
        }

    if predicted_cost == 0:
        discrepancy_percentage = 0
    else:
        discrepancy_percentage = (
            abs(cost_difference) / predicted_cost
        ) * 100

    # 20% discrepancy threshold
    should_retrain = discrepancy_percentage >= 20

    return {
        "should_retrain": should_retrain,
        "predicted_cost": predicted_cost,
        "actual_cost": actual_cost,
        "cost_difference": cost_difference,
        "discrepancy_percentage": round(
            discrepancy_percentage,
            2
        ),
        "outcome": outcome
    }


def retrain_model():
    """
    Retrain the XGBoost model using the
    historical supply-chain dataset.
    """

    df = pd.read_csv(
        DATASET_PATH,
        encoding="latin1"
    )

    df = df.drop(
        columns=[
            "Product Description",
            "Order Zipcode"
        ],
        errors="ignore"
    )

    if "Customer Lname" in df.columns:
        df["Customer Lname"] = (
            df["Customer Lname"].fillna("Unknown")
        )

    if "Customer Zipcode" in df.columns:
        df["Customer Zipcode"] = (
            df["Customer Zipcode"].fillna(0)
        )

    features = [
        "Days for shipment (scheduled)",
        "Benefit per order",
        "Sales per customer",
        "Category Id",
        "Order Item Quantity",
        "Product Price",
        "Shipping Mode",
        "Market",
        "Order Region"
    ]

    target = "Late_delivery_risk"

    X = df[features].copy()
    y = df[target]

    encoders = {}

    for col in X.select_dtypes(
        include="object"
    ).columns:

        encoder = LabelEncoder()

        X[col] = encoder.fit_transform(
            X[col].astype(str)
        )

        encoders[col] = encoder

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = XGBClassifier(
        random_state=42,
        n_estimators=100,
        max_depth=5,
        learning_rate=0.1,
        eval_metric="logloss"
    )

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    joblib.dump(
        model,
        MODEL_PATH
    )

    joblib.dump(
        encoders,
        ENCODER_PATH
    )

    return {
        "success": True,
        "message": "XGBoost model retrained successfully",
        "accuracy": round(
            accuracy * 100,
            2
        )
    }


def continuous_learning(decision_id):
    """
    Check a decision for discrepancy and
    retrain the model when necessary.
    """

    discrepancy = check_discrepancy(
        decision_id
    )

    if not discrepancy.get(
        "should_retrain",
        False
    ):

        return {
            "retrained": False,
            "discrepancy": discrepancy,
            "message":
                "No significant discrepancy detected. "
                "Retraining not required."
        }

    training_result = retrain_model()

    return {
        "retrained": True,
        "discrepancy": discrepancy,
        "training": training_result,
        "message":
            "Significant discrepancy detected. "
            "XGBoost model retrained automatically."
    }