import sqlite3


DB_NAME = "supplyprescript.db"


conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS decisions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    shipment_id TEXT,
    prediction TEXT,
    action TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")


cursor.execute("PRAGMA table_info(decisions)")
existing_columns = [column[1] for column in cursor.fetchall()]


new_columns = {
    "predicted_cost": "REAL",
    "actual_cost": "REAL",
    "cost_difference": "REAL",
    "outcome": "TEXT",
    "evaluated": "INTEGER DEFAULT 0"
}


for column_name, column_type in new_columns.items():

    if column_name not in existing_columns:

        cursor.execute(
            f"ALTER TABLE decisions ADD COLUMN {column_name} {column_type}"
        )


conn.commit()
conn.close()


print("Database Updated Successfully")