function RecommendationCard({ recommendations, onSave }) {
  return (
    <div
      style={{
        background: "#1f2937",
        padding: "20px",
        borderRadius: "12px",
        marginTop: "25px",
      }}
    >
      <h2>🤖 AI Recommendations</h2>

      {recommendations.length === 0 ? (
        <p>No recommendations yet.</p>
      ) : (
        recommendations.map((item, index) => (
          <div
            key={index}
            style={{
              background: "#374151",
              padding: "15px",
              borderRadius: "10px",
              marginTop: "15px",
            }}
          >
            <h3>{item.title}</h3>

            <p>{item.description}</p>

            <p>
              <b>Cost:</b> ${item.cost}
            </p>

            <p>
              <b>Delivery:</b> {item.delivery_days} Days
            </p>

            <p>
              <b>Risk:</b> {item.risk}
            </p>

            <button
              onClick={() => onSave(item)}
              style={{
                marginTop: "10px",
                padding: "8px 15px",
              }}
            >
              Execute Decision
            </button>
          </div>
        ))
      )}
    </div>
  );
}

export default RecommendationCard;