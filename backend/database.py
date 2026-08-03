import sqlite3

conn = sqlite3.connect("supplyprescript.db")

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

conn.commit()
conn.close()

print("Database Created Successfully")