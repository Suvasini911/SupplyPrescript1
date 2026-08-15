# 🚚 SupplyPrescript AI

## AI-Powered Supply Chain Decision Support System

SupplyPrescript AI is a data-driven supply chain decision-support system that predicts shipment delay risk, provides actionable recommendations, evaluates executed decisions, calculates decision ROI, and supports continuous model learning.

The project was developed as the **Month 1 Data Analytics Internship Project**, covering Weeks 1–4.

---

## 🎯 Project Overview

Supply-chain operations can be affected by shipment delays, unexpected costs, and inefficient decisions.

SupplyPrescript AI uses historical supply-chain data and machine learning to help users:

- Predict shipment delay risk
- Generate supply-chain recommendations
- Execute and record decisions
- Compare predicted and actual costs
- Measure decision performance
- Automatically retrain the model when significant discrepancies occur

---

## 📅 Project Progress

### Week 1 — Data Cleaning

- Loaded and explored the raw supply-chain dataset
- Identified missing and unnecessary data
- Cleaned and prepared the dataset
- Created a cleaned dataset for further analysis

Notebook:

```text
notebooks/01_Data_Cleaning.ipynb
````

---

### Week 2 — Exploratory Data Analysis

Performed exploratory analysis to understand:

* Shipment and delivery patterns
* Order quantity
* Product price
* Sales and benefits
* Shipping modes
* Markets
* Order regions
* Delivery risk

Notebook:

```text
notebooks/02_EDA.ipynb
```

---

### Week 3 — Decision Support & Feedback

The system was extended from simple prediction to a complete decision-support workflow.

#### Shipment Prediction

The user enters shipment information through the React dashboard.

The XGBoost model predicts:

```text
High Delay Risk
```

or

```text
Low Delay Risk
```

#### AI Recommendations

Based on the prediction, the system provides possible actions such as:

* Use Air Freight
* Use Standard Shipping
* Switch to Secondary Supplier
* Proceed Normally

Each recommendation contains information such as cost, delivery time, and risk.

#### Decision Execution

Users can execute a selected recommendation.

The decision is stored in the SQLite database.

#### Decision Feedback

The system allows the user to enter the actual cost after a decision.

It compares:

```text
Predicted Cost
       vs
Actual Cost
```

and calculates:

* Cost Difference
* Outcome
* Evaluation Status

#### Decision ROI

The dashboard provides:

* Total Decisions
* Positive Decisions
* Positive Rate
* Average Cost Difference

---

### Week 4 — Continuous Learning

A continuous-learning mechanism was added to the decision workflow.

After a decision is evaluated, the system calculates the cost discrepancy.

The configured retraining threshold is:

```text
20%
```

If the discrepancy reaches or exceeds the threshold, the XGBoost model is automatically retrained using the historical supply-chain data.

### Workflow

```text
Decision Evaluation
        ↓
Calculate Cost Discrepancy
        ↓
Compare with 20% Threshold
        ↓
Significant Discrepancy?
       / \
     YES  NO
      ↓    ↓
 Retrain  Continue
  Model
      ↓
Updated Model
```

A test case produced:

```text
Predicted Cost = $8,000
Actual Cost    = $1,000
Discrepancy    = 87.5%
```

Since:

```text
87.5% > 20%
```

the system automatically triggered XGBoost retraining.

The retraining process reported a new model accuracy of:

```text
69.16%
```

The result is displayed in the frontend through the **Continuous Learning** section.

---

# 🤖 Machine Learning

The project uses an **XGBoost** model for shipment delay-risk prediction.

### Prediction Features

The model uses shipment-related features including:

* Scheduled shipment days
* Benefit per order
* Sales per customer
* Category ID
* Order quantity
* Product price
* Shipping mode
* Market
* Order region

---

# 🖥️ Dashboard Features

The React dashboard provides:

* 📦 Shipment prediction
* 🤖 AI recommendations
* 📋 Decision history
* 📊 Analytics
* 💰 Decision ROI
* 🔄 Decision feedback
* 🧠 Continuous learning

---

# 🔄 Complete System Workflow

```text
Historical Supply Chain Data
            ↓
       Data Cleaning
            ↓
      Exploratory Analysis
            ↓
       ML Prediction
            ↓
    AI Recommendations
            ↓
      Execute Decision
            ↓
       Store Decision
            ↓
      Actual Cost Input
            ↓
     Decision Evaluation
            ↓
       Decision ROI
            ↓
    Discrepancy Detection
            ↓
 Automatic Model Retraining
```

---

# 🛠️ Technology Stack

### Data Analytics & Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Joblib

### Backend

* FastAPI
* Pydantic
* SQLite

### Frontend

* React
* JavaScript
* Axios

### Development

* VS Code
* Git
* GitHub

---

# 📁 Project Structure

```text
SupplyPrescript/
│
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── optimizer.py
│   ├── evaluation.py
│   ├── continuous_learning.py
│   ├── model.pkl
│   ├── encoder.pkl
│   └── supplyprescript.db
│
├── dataset/
│   ├── supply_chain_data.csv
│   └── cleaned_supply_chain_data.csv
│
├── frontend/
│   └── src/
│       ├── components/
│       └── pages/
│
├── notebooks/
│   ├── 01_Data_Cleaning.ipynb
│   └── 02_EDA.ipynb
│
└── README.md
```

---

# 🚀 How to Run

## Backend

Open a terminal:

```powershell
cd backend
```

Activate the virtual environment:

```powershell
..\venv\Scripts\Activate.ps1
```

Run FastAPI:

```powershell
python -m uvicorn app:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

---

## Frontend

Open another terminal:

```powershell
cd frontend
```

Run:

```powershell
npm run dev
```

Open the localhost URL shown by Vite.

---

# 🗄️ Database

SQLite is used to store decision information.

The decision records include:

* Decision ID
* Shipment ID
* Prediction
* Action
* Predicted Cost
* Actual Cost
* Cost Difference
* Outcome
* Evaluation Status

---

# 📊 Project Outcome

SupplyPrescript AI demonstrates a complete data-driven decision-support cycle:

```text
Data
 ↓
Analysis
 ↓
Prediction
 ↓
Recommendation
 ↓
Decision
 ↓
Feedback
 ↓
Evaluation
 ↓
Learning
```

The project extends a traditional ML prediction system by connecting predictions with actual decision outcomes and using significant discrepancies to trigger model retraining.

---

# 🔮 Future Scope

* Real-time shipment tracking
* Live logistics API integration
* Advanced cost optimization
* Improved recommendation algorithms
* Model performance monitoring
* Cloud deployment
* User authentication
* Advanced supply-chain analytics

---

## 👩‍💻 Project

**SupplyPrescript AI**

**AI-Powered Supply Chain Decision Support System**

**Data Analytics Internship — Month 1 Project**