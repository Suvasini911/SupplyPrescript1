function ContinuousLearning({ learning }) {
  if (!learning) {
    return null;
  }

  const discrepancy =
    learning.discrepancy?.discrepancy_percentage ?? 0;

  const retrained =
    learning.retrained === true;

  const accuracy =
    learning.training?.accuracy;

  return (
    <div
      style={{
        background: "#1f2937",
        padding: "20px",
        borderRadius: "12px",
        marginTop: "25px",
      }}
    >
      <h2 style={{ textAlign: "center" }}>
        🧠 Continuous Learning
      </h2>

      <p
        style={{
          textAlign: "center",
          color: "#9CA3AF",
        }}
      >
        The AI model learns from evaluated shipment outcomes.
      </p>

      <div
        style={{
          background: "#374151",
          padding: "18px",
          borderRadius: "10px",
          marginTop: "15px",
        }}
      >
        <p>
          <b>Cost Discrepancy:</b>{" "}
          {discrepancy}%
        </p>

        <p>
          <b>Retraining Threshold:</b> 20%
        </p>

        <p>
          <b>Retraining Status:</b>{" "}
          <span
            style={{
              color: retrained
                ? "#22c55e"
                : "#facc15",
              fontWeight: "bold",
            }}
          >
            {retrained
              ? "Model Retrained Automatically"
              : "Retraining Not Required"}
          </span>
        </p>

        {accuracy !== undefined && (
          <p>
            <b>New Model Accuracy:</b>{" "}
            {accuracy}%
          </p>
        )}

        <p
          style={{
            color: "#9CA3AF",
            fontSize: "14px",
          }}
        >
          {learning.message}
        </p>
      </div>
    </div>
  );
}

export default ContinuousLearning;