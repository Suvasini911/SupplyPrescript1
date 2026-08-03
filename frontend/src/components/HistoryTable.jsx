import { useEffect, useState } from "react";

function HistoryTable() {

  const [history, setHistory] = useState([]);

  useEffect(() => {

    fetch("http://127.0.0.1:8000/history")
      .then((res) => res.json())
      .then((data) => {
        setHistory(data);
      });

  }, []);

  return (

    <div
      style={{
        background: "#1f2937",
        padding: "20px",
        borderRadius: "12px",
        marginTop: "25px",
      }}
    >

      <h2>📜 Decision History</h2>

      {history.length === 0 ? (

        <p>No history available.</p>

      ) : (

        <table
          style={{
            width: "100%",
            marginTop: "20px",
            borderCollapse: "collapse",
          }}
        >

          <thead>

            <tr>

              <th>ID</th>

              <th>Prediction</th>

              <th>Action</th>

            </tr>

          </thead>

          <tbody>

            {history.map((row, index) => (

              <tr key={index}>

                <td>{row[0]}</td>

                <td>{row[2]}</td>

                <td>{row[3]}</td>

              </tr>

            ))}

          </tbody>

        </table>

      )}

    </div>

  );

}

export default HistoryTable;