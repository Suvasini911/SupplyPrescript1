import { useState } from "react";
import axios from "axios";

function ShipmentForm({ setPrediction, setRecommendations }) {
  const [form, setForm] = useState({
    scheduled_days: 4,
    benefit_per_order: 35.5,
    sales_per_customer: 120,
    category_id: 17,
    quantity: 2,
    product_price: 60,
    shipping_mode: "Standard Class",
    market: "Pacific Asia",
    order_region: "Western Europe",
  });

  const [result, setResult] = useState("");

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]:
        e.target.type === "number"
          ? Number(e.target.value)
          : e.target.value,
    });
  };

  const predict = async () => {
    try {
      const res = await axios.post(
      "http://127.0.0.1:8000/predict",
      form
    );

    // Update ShipmentForm
    setResult(res.data.prediction_text);

    // Update Dashboard
    setPrediction(res.data.prediction_text);
    setRecommendations(res.data.recommendations);

  } catch (err) {
    console.error(err);
    alert("Prediction Failed");
    }
  };

  return (
    <div
      style={{
        background: "#1f2937",
        padding: "20px",
        borderRadius: "12px",
        marginTop: "30px",
      }}
    >
      <h2>Shipment Details</h2>

      <input
        type="number"
        name="scheduled_days"
        placeholder="Scheduled Days"
        value={form.scheduled_days}
        onChange={handleChange}
      />

      <input
        type="number"
        name="quantity"
        placeholder="Quantity"
        value={form.quantity}
        onChange={handleChange}
      />

      <br /><br />

      <button onClick={predict}>
        Predict Shipment
      </button>

      <h3 style={{ marginTop: "20px" }}>
        Prediction:
        <span
          style={{
            color:
              result === "High Delay Risk"
                ? "red"
                : "lime",
            marginLeft: "10px",
          }}
        >
          {result}
        </span>
      </h3>
    </div>
  );
}

export default ShipmentForm;

// Shipment prediction form