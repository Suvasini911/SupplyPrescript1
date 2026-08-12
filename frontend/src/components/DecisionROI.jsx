import { useEffect, useState } from "react";

function DecisionROI() {
  const [roi, setRoi] = useState(null);

  const loadROI = async () => {
    try {
      const response = await fetch(
        "http://127.0.0.1:8000/decision-roi"
      );

      const data = await response.json();

      setRoi(data);
    } catch (error) {
      console.error("Failed to load Decision ROI:", error);
    }
  };

  useEffect(() => {
    loadROI();
  }, []);

  if (!roi) {
    return (
      <div
        style={{
          background: "#1f2937",
          padding: "20px",
          borderRadius: "12px",
          marginTop: "25px",
        }}
      >
        <h2>📊 Decision ROI</h2>
        <p>Loading ROI...</p>
      </div>
    );
  }

  return (
    <div
      style={{
        background: "#1f2937",
        padding: "20px",
        borderRadius: "12px",
        marginTop: "25px",
      }}
    >
      <h2>📊 Decision ROI</h2>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(4, 1fr)",
          gap: "15px",
          marginTop: "20px",
        }}
      >
        <div
          style={{
            background: "#374151",
            padding: "15px",
            borderRadius: "10px",
          }}
        >
          <h3>Total Decisions</h3>
          <p style={{ fontSize: "24px" }}>
            {roi.total_decisions}
          </p>
        </div>

        <div
          style={{
            background: "#374151",
            padding: "15px",
            borderRadius: "10px",
          }}
        >
          <h3>Positive Decisions</h3>
          <p style={{ fontSize: "24px" }}>
            {roi.positive_decisions}
          </p>
        </div>

        <div
          style={{
            background: "#374151",
            padding: "15px",
            borderRadius: "10px",
          }}
        >
          <h3>Positive Rate</h3>
          <p style={{ fontSize: "24px" }}>
            {roi.positive_rate}%
          </p>
        </div>

        <div
          style={{
            background: "#374151",
            padding: "15px",
            borderRadius: "10px",
          }}
        >
          <h3>Avg Cost Difference</h3>
          <p style={{ fontSize: "24px" }}>
            ${roi.average_cost_difference}
          </p>
        </div>
      </div>
    </div>
  );
}

export default DecisionROI;