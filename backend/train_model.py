import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
import joblib

# Load dataset
df = pd.read_csv("../dataset/supply_chain_data.csv", encoding="latin1")

# Remove unnecessary columns
df = df.drop(columns=["Product Description", "Order Zipcode"], errors="ignore")

# Fill missing values
df["Customer Lname"] = df["Customer Lname"].fillna("Unknown")
df["Customer Zipcode"] = df["Customer Zipcode"].fillna(0)

# Features
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

# Encode categorical columns
encoders = {}

for col in X.select_dtypes(include="object").columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))
    encoders[col] = le

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = XGBClassifier(
    random_state=42,
    n_estimators=100,
    max_depth=5,
    learning_rate=0.1,
    eval_metric="logloss"
)

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"\nModel Accuracy: {accuracy*100:.2f}%")

# Save model and encoders
joblib.dump(model, "model.pkl")
joblib.dump(encoders, "encoder.pkl")

print("Model saved as model.pkl")
print("Encoders saved as encoder.pkl")