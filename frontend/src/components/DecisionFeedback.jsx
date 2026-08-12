import { useEffect, useState } from "react";

function DecisionFeedback({ onEvaluated }) {

  const [decisions, setDecisions] = useState([]);

  const [decisionId, setDecisionId] = useState("");

  const [actualCost, setActualCost] = useState("");

  const [result, setResult] = useState(null);

  const [loading, setLoading] = useState(false);


  const loadDecisions = async () => {

    try {

      const response = await fetch(
        "http://127.0.0.1:8000/history"
      );

      const data = await response.json();


      const formatted = data.map((row) => ({
        id: row[0],
        shipment_id: row[1],
        prediction: row[2],
        action: row[3],
        created_at: row[4],
        predicted_cost: row[5],
        actual_cost: row[6],
        cost_difference: row[7],
        outcome: row[8],
        evaluated: row[9],
      }));


      setDecisions(formatted);

    } catch (error) {

      console.error(
        "Failed to load decisions:",
        error
      );

    }

  };


  useEffect(() => {

    loadDecisions();

  }, []);


  const evaluateDecision = async () => {

    if (!decisionId || !actualCost) {

      alert(
        "Please select a decision and enter actual cost."
      );

      return;

    }


    setLoading(true);

    setResult(null);


    try {

      const response = await fetch(
        "http://127.0.0.1:8000/evaluate-decision",
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json",
          },

          body: JSON.stringify({

            decision_id: Number(decisionId),

            actual_cost: Number(actualCost),

          }),

        }
      );


      const data = await response.json();


      console.log(
        "Evaluation Response:",
        data
      );


      setResult(data);


      /*
       * Send the Week 4 continuous-learning
       * result back to Dashboard.jsx
       */

      if (onEvaluated) {

        onEvaluated(data);

      }


      await loadDecisions();


    } catch (error) {

      console.error(
        "Evaluation failed:",
        error
      );

      alert(
        "Evaluation failed."
      );

    } finally {

      setLoading(false);

    }

  };


  return (

    <div
      style={{
        background: "#1f2937",
        padding: "20px",
        borderRadius: "12px",
        marginTop: "25px",
      }}
    >

      <h2>
        🔄 Decision Feedback
      </h2>


      <p
        style={{
          color: "#9CA3AF",
        }}
      >
        Compare the AI predicted cost with
        the actual shipment outcome.
      </p>


      {/* Decision Selection */}

      <div
        style={{
          marginTop: "20px",
        }}
      >

        <label>
          <b>Decision:</b>
        </label>


        <select
          value={decisionId}
          onChange={(e) =>
            setDecisionId(e.target.value)
          }
          style={{
            display: "block",
            marginTop: "8px",
            padding: "10px",
            width: "100%",
          }}
        >

          <option value="">
            Select a decision
          </option>


          {decisions
            .filter(
              (decision) =>
                decision.evaluated !== 1
            )
            .map((decision) => (

              <option
                key={decision.id}
                value={decision.id}
              >

                #{decision.id} -{" "}
                {decision.action} - $
                {decision.predicted_cost ?? "N/A"}

              </option>

            ))}

        </select>

      </div>


      {/* Actual Cost */}

      <div
        style={{
          marginTop: "20px",
        }}
      >

        <label>
          <b>Actual Cost:</b>
        </label>


        <input
          type="number"
          placeholder="Enter actual cost"
          value={actualCost}
          onChange={(e) =>
            setActualCost(e.target.value)
          }
          style={{
            display: "block",
            marginTop: "8px",
            padding: "10px",
            width: "100%",
            boxSizing: "border-box",
          }}
        />

      </div>


      {/* Evaluate Button */}

      <button
        onClick={evaluateDecision}
        disabled={loading}
        style={{
          marginTop: "20px",
          padding: "10px 18px",
          cursor: "pointer",
        }}
      >

        {loading
          ? "Evaluating..."
          : "Evaluate Decision"}

      </button>


      {/* Evaluation Result */}

      {result && result.success && (

        <div
          style={{
            background: "#374151",
            padding: "20px",
            borderRadius: "10px",
            marginTop: "20px",
          }}
        >

          <h3>
            📊 Evaluation Result
          </h3>


          <p>
            <b>Decision:</b>{" "}
            {result.action}
          </p>


          <p>
            <b>Predicted Cost:</b>{" "}
            ${result.predicted_cost}
          </p>


          <p>
            <b>Actual Cost:</b>{" "}
            ${result.actual_cost}
          </p>


          <p>
            <b>Cost Difference:</b>{" "}
            ${result.cost_difference}
          </p>


          <p>
            <b>Outcome:</b>{" "}

            <span
              style={{
                color:
                  result.outcome === "Positive"
                    ? "#22c55e"
                    : "#ef4444",

                fontWeight: "bold",
              }}
            >

              {result.outcome}

            </span>

          </p>


          {/* Week 4 Result */}

          {result.continuous_learning && (

            <div
              style={{
                marginTop: "20px",
                padding: "15px",
                background: "#111827",
                borderRadius: "8px",
              }}
            >

              <h3>
                🧠 Continuous Learning Result
              </h3>


              <p>
                <b>Retraining:</b>{" "}

                {result.continuous_learning.retrained
                  ? "Triggered Automatically ✅"
                  : "Not Required"}
              </p>


              {result.continuous_learning
                .discrepancy && (

                <p>
                  <b>Discrepancy:</b>{" "}

                  {
                    result
                      .continuous_learning
                      .discrepancy
                      .discrepancy_percentage
                  }
                  %
                </p>

              )}


              {result.continuous_learning
                .training?.accuracy !==
                undefined && (

                <p>
                  <b>New Model Accuracy:</b>{" "}

                  {
                    result
                      .continuous_learning
                      .training
                      .accuracy
                  }
                  %
                </p>

              )}


              <p
                style={{
                  color: "#9CA3AF",
                  fontSize: "14px",
                }}
              >

                {
                  result
                    .continuous_learning
                    .message
                }

              </p>

            </div>

          )}

        </div>

      )}


      {result &&
        !result.success && (

          <p
            style={{
              color: "#ef4444",
              marginTop: "15px",
            }}
          >

            {result.message}

          </p>

        )}

    </div>

  );

}


export default DecisionFeedback;