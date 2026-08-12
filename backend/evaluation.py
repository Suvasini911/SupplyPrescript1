import sqlite3


DB_NAME = "supplyprescript.db"


def evaluate_decision(decision_id, actual_cost):
    """
    Compare the predicted cost of a decision
    with its actual historical cost.
    """

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Get the selected decision
    cursor.execute("""
        SELECT predicted_cost, action
        FROM decisions
        WHERE id = ?
    """, (decision_id,))

    decision = cursor.fetchone()

    if decision is None:
        conn.close()
        return {
            "success": False,
            "message": "Decision not found"
        }

    predicted_cost = decision[0]
    action = decision[1]

    # Calculate cost difference
    cost_difference = actual_cost - predicted_cost

    # Positive business outcome:
    # actual cost is less than or equal to predicted cost
    if actual_cost <= predicted_cost:
        outcome = "Positive"
    else:
        outcome = "Negative"

    # Update database
    cursor.execute("""
        UPDATE decisions
        SET actual_cost = ?,
            cost_difference = ?,
            outcome = ?,
            evaluated = 1
        WHERE id = ?
    """, (
        actual_cost,
        cost_difference,
        outcome,
        decision_id
    ))

    conn.commit()
    conn.close()

    return {
        "success": True,
        "decision_id": decision_id,
        "action": action,
        "predicted_cost": predicted_cost,
        "actual_cost": actual_cost,
        "cost_difference": cost_difference,
        "outcome": outcome
    }


def get_decision_roi():
    """
    Calculate Decision ROI statistics
    from evaluated decisions.
    """

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            COUNT(*) AS total_decisions,
            SUM(
                CASE
                    WHEN outcome = 'Positive' THEN 1
                    ELSE 0
                END
            ) AS positive_decisions,
            AVG(cost_difference) AS average_cost_difference
        FROM decisions
        WHERE evaluated = 1
    """)

    result = cursor.fetchone()

    conn.close()

    total_decisions = result[0] or 0
    positive_decisions = result[1] or 0
    average_cost_difference = result[2] or 0

    if total_decisions > 0:
        positive_rate = (
            positive_decisions / total_decisions
        ) * 100
    else:
        positive_rate = 0

    return {
        "total_decisions": total_decisions,
        "positive_decisions": positive_decisions,
        "positive_rate": round(positive_rate, 2),
        "average_cost_difference": round(
            average_cost_difference, 2
        )
    }