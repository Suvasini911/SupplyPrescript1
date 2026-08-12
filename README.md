# 🚚 SupplyPrescript AI

## Overview

SupplyPrescript AI is an AI-powered supply chain decision-support system.

The system uses historical supply-chain data to analyze shipment information, predict shipment delay risk using machine learning, and provide recommendations to help users make better supply-chain decisions.

---

## Business Problem

Shipment delays can affect customer satisfaction, operational efficiency, and business costs.

SupplyPrescript AI addresses this problem by analyzing historical shipment and order data to:

- Identify shipment delay patterns
- Predict shipment delay risk
- Provide actionable recommendations
- Allow users to execute recommended decisions
- Store executed decisions for future reference
- Display shipment analytics and decision history

---

## Project Objectives

The main objectives of SupplyPrescript AI are:

1. Analyze historical supply-chain data.
2. Clean and prepare the dataset for analysis.
3. Perform exploratory data analysis (EDA).
4. Build a machine-learning based shipment delay-risk prediction system.
5. Generate recommendations based on prediction results.
6. Provide an interactive dashboard for users.
7. Store executed decisions using SQLite.
8. Display decision history and analytics.

---

# 📊 Dataset

The project uses a supply-chain dataset containing information related to:

- Shipment duration
- Scheduled shipment duration
- Product price
- Order quantity
- Sales
- Customer information
- Product information
- Delivery risk
- Order information
- Profit information

### Dataset Files

```text
dataset/
├── supply_chain_data.csv
└── cleaned_supply_chain_data.csv
📌 Week 1 — Data Preparation

During Week 1, the dataset was loaded and prepared for further analysis.

Data Preparation Tasks
Loaded the dataset using Pandas
Inspected the dataset structure
Checked the number of rows and columns
Inspected column names
Checked data types
Checked for missing values
Checked for duplicate records
Removed duplicate records where applicable
Standardized column names
Created a cleaned dataset
Data Cleaning Notebook
notebooks/01_Data_Cleaning.ipynb
Data Cleaning Workflow
Raw Dataset
     ↓
Data Ingestion
     ↓
Dataset Inspection
     ↓
Missing Value Check
     ↓
Duplicate Check
     ↓
Data Type Check
     ↓
Data Cleaning
     ↓
Cleaned Dataset
📈 Week 2 — Exploratory Data Analysis

During Week 2, Exploratory Data Analysis (EDA) was performed on the cleaned dataset.

Statistical Analysis

The following statistical measures were analyzed:

Descriptive statistics
Mean
Median
Standard deviation
Data Analysis

The analysis included:

Distribution of product prices
Comparison of scheduled and actual shipping duration
Outlier analysis
Correlation analysis
Shipping delay analysis
Visualizations

The following visualizations were created:

Product price distribution histogram
Scheduled vs actual shipping duration scatter plot
Boxplot for outlier analysis
Feature correlation matrix
Shipping delay distribution
EDA Notebook
notebooks/02_EDA.ipynb
Shipping Delay Calculation

Shipping delay was calculated using:

Shipping Delay = Actual Shipping Days - Scheduled Shipping Days

This analysis helps identify shipment delay patterns and provides a foundation for the machine-learning prediction stage.

🤖 Machine Learning

SupplyPrescript AI uses a trained machine-learning model to predict shipment delay risk.

Prediction Workflow
Shipment Details
       ↓
Data Preprocessing
       ↓
Machine Learning Model
       ↓
Delay Risk Prediction
       ↓
Recommendation Engine
       ↓
Business Recommendation

The model predicts whether a shipment has:

High Delay Risk
Low Delay Risk
💡 Recommendation System

After the shipment risk is predicted, the system generates recommendations based on the prediction.

The recommendation system helps the user decide what action should be taken for the shipment.

The user can review the recommendation and execute the selected decision.

💾 Decision Storage

SupplyPrescript AI uses SQLite to store executed decisions.

The workflow is:

Prediction
    ↓
Recommendation
    ↓
Execute Decision
    ↓
SQLite Database
    ↓
Decision History

The saved decisions can later be retrieved and displayed in the dashboard.

📊 Dashboard

The React dashboard provides an interactive interface for the complete workflow.

Dashboard Features
Shipment input form
Shipment delay prediction
AI recommendations
Execute Decision functionality
Decision history
Analytics visualization
Shipment-risk information
🔄 Complete Application Workflow
User enters shipment details
          ↓
React Frontend
          ↓
FastAPI Backend
          ↓
Data Preprocessing
          ↓
Machine Learning Model
          ↓
Delay Risk Prediction
          ↓
Recommendation Engine
          ↓
User Executes Decision
          ↓
SQLite Database
          ↓
Decision History
          ↓
Analytics Dashboard
🛠️ Technology Stack
Frontend
React
Vite
Axios
JavaScript
CSS
Backend
FastAPI
Python
SQLite
Pandas
Scikit-learn
Joblib
Data Analysis
Pandas
NumPy
Matplotlib
Seaborn
Machine Learning
Scikit-learn
Joblib
Version Control
Git
GitHub
📁 Project Structure
SupplyPrescript/
│
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── optimizer.py
│   ├── predict.py
│   ├── train_model.py
│   ├── model.pkl
│   ├── encoder.pkl
│   ├── supplyprescript.db
│   └── requirements.txt
│
├── dataset/
│   ├── supply_chain_data.csv
│   └── cleaned_supply_chain_data.csv
│
├── notebooks/
│   ├── 01_Data_Cleaning.ipynb
│   └── 02_EDA.ipynb
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── screenshots/
│
├── README.md
└── .gitignore
🚀 How to Run the Project
1. Backend Setup

Open a terminal and navigate to the backend folder:

cd backend

Activate the Python virtual environment if required.

Then start the FastAPI server:

uvicorn app:app --reload

The backend will run at:

http://127.0.0.1:8000
2. Frontend Setup

Open another terminal and navigate to the frontend folder:

cd frontend

Install the required packages:

npm install

Start the React development server:

npm run dev

The frontend will normally run at:

http://localhost:5173
🧪 Data Analysis Notebooks
Data Cleaning

The 01_Data_Cleaning.ipynb notebook contains:

Dataset loading
Dataset inspection
Data type analysis
Missing value checking
Duplicate checking
Data cleaning
Cleaned dataset generation
Exploratory Data Analysis

The 02_EDA.ipynb notebook contains:

Descriptive statistics
Mean calculation
Median calculation
Standard deviation
Outlier analysis
Histogram
Scatter plot
Correlation matrix
Shipping delay analysis
📌 Current Implementation Status
Week 1
✅ Dataset selection
✅ Data ingestion
✅ Dataset inspection
✅ Data type analysis
✅ Missing value analysis
✅ Duplicate analysis
✅ Data cleaning
✅ Cleaned dataset generation
Week 2
✅ Exploratory Data Analysis
✅ Descriptive statistics
✅ Mean analysis
✅ Median analysis
✅ Standard deviation analysis
✅ Outlier analysis
✅ Histogram visualization
✅ Scatter plot visualization
✅ Correlation analysis
✅ Shipping delay analysis
Application
✅ React dashboard
✅ FastAPI backend
✅ Machine-learning prediction
✅ Recommendation system
✅ SQLite decision storage
✅ Decision history
✅ Analytics visualization
🎯 Future Improvements

The project can be further improved by:

Improving the machine-learning model
Adding more advanced predictive features
Improving recommendation optimization
Adding more dashboard analytics
Improving UI/UX
Adding additional business metrics
Improving model evaluation and monitoring
👩‍💻 Author

Suvasini 

Computer Science & Engineering