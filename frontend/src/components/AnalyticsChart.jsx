import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend,
} from "recharts";

const data = [
  { name: "Low Risk", value: 70 },
  { name: "High Risk", value: 30 },
];

const COLORS = ["#22c55e", "#ef4444"];

function AnalyticsChart() {
  return (
    <div
      style={{
        background: "#1f2937",
        padding: "20px",
        borderRadius: "12px",
        marginTop: "25px",
        textAlign: "center",
      }}
    >
      <h2>📊 Analytics</h2>

      <PieChart width={500} height={300}>
        <Pie
          data={data}
          cx={220}
          cy={130}
          outerRadius={90}
          dataKey="value"
          label
        >
          {data.map((entry, index) => (
            <Cell
              key={index}
              fill={COLORS[index]}
            />
          ))}
        </Pie>

        <Tooltip />

        <Legend />
      </PieChart>
    </div>
  );
}

export default AnalyticsChart;