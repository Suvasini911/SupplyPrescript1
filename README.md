# 🚚 SupplyPrescript AI

## Overview
SupplyPrescript AI is an AI-powered supply chain optimization system.

## Features
- Shipment delay prediction
- AI recommendations
- Decision history
- Analytics dashboard

## Tech Stack
- React
- FastAPI
- Python
- SQLite
- Machine Learning

### Frontend
- React
- Vite
- Axios

### Backend
- FastAPI
- Python
- SQLite
- Scikit-learn
- Pandas

## Project Structure

```
SupplyPrescript/
│
├── backend/
│   ├── app.py
│   ├── optimizer.py
│   ├── train_model.py
│   └── supplyprescript.db
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── dataset/
│   └── supply_chain_data.csv
│
└── README.md
```

## Workflow

1. User enters shipment details.
2. React sends data to FastAPI.
3. Machine Learning model predicts shipment delay risk.
4. Optimizer generates recommendations.
5. User executes a recommendation.
6. Decision is stored in SQLite.
7. Dashboard displays analytics and history.

## How to Run

### Backend

```bash
cd backend
uvicorn app:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Current Progress

- ✅ Week 1 Completed
- ✅ Week 2 Completed

## Author

Suvasini G