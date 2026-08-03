function DashboardCards() {
  const cards = [
    {
      title: "Total Shipments",
      value: "180,519",
      color: "#2563eb",
    },
    {
      title: "High Risk Orders",
      value: "34,102",
      color: "#dc2626",
    },
    {
      title: "Estimated Savings",
      value: "$1.2M",
      color: "#16a34a",
    },
    {
      title: "AI Accuracy",
      value: "92%",
      color: "#9333ea",
    },
  ];

  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: "repeat(4,1fr)",
        gap: "20px",
        marginBottom: "30px",
      }}
    >
      {cards.map((card, index) => (
        <div
          key={index}
          style={{
            background: card.color,
            color: "white",
            padding: "20px",
            borderRadius: "12px",
            textAlign: "center",
            boxShadow: "0 5px 10px rgba(0,0,0,0.2)",
          }}
        >
          <h3>{card.title}</h3>

          <h1>{card.value}</h1>
        </div>
      ))}
    </div>
  );
}

export default DashboardCards;