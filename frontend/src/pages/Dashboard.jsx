import { useState } from "react";

import DashboardCards from "../components/DashboardCards";
import ShipmentForm from "../components/ShipmentForm";
import RecommendationCard from "../components/RecommendationCard";
import HistoryTable from "../components/HistoryTable";
import AnalyticsChart from "../components/AnalyticsChart";

function Dashboard() {

  const [recommendations, setRecommendations] = useState([]);

  const [prediction, setPrediction] = useState("");

  const saveDecision = async (item) => {

  try {

    const response = await fetch(
      "http://127.0.0.1:8000/save-decision",
      {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify({

          shipment_id: 1,

          prediction: prediction,

          action: item.title

        }),

      }
    );

    const data = await response.json();

    alert(data.message);

  } catch (err) {

    console.error(err);

    alert("Save Failed");

  }

};

  return (

    <div
      style={{
        maxWidth: "1200px",
        margin: "20px auto",
        padding: "20px",
      }}
    >

      <h1
        style={{
          textAlign: "center",
          marginBottom: "30px",
        }}
      >
        🚚 SupplyPrescript AI Dashboard
      </h1>

      <DashboardCards />

      <ShipmentForm
        setPrediction={setPrediction}
        setRecommendations={setRecommendations}
      />

      <RecommendationCard
  recommendations={recommendations}
  onSave={saveDecision}
/>

      <HistoryTable />

      <AnalyticsChart />

    </div>

  );

}

export default Dashboard;