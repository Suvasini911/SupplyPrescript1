from scipy.optimize import linprog


# Business constraint
# Maximum budget allowed for a high-risk shipment
MAX_BUDGET = 15000


def get_recommendations(delay_risk):

    # If shipment is low risk, no optimization is required
    if delay_risk == 0:
        return [
            {
                "title": "Proceed Normally",
                "description": "Shipment is expected to arrive on time.",
                "cost": 0,
                "delivery_days": 0,
                "risk": "None"
            }
        ]

    # ---------------------------------------------------------
    # Available actions
    # ---------------------------------------------------------
    actions = [
        {
            "title": "Use Air Freight",
            "description": "Fastest delivery option to reduce shipment delay.",
            "cost": 15000,
            "delivery_days": 2,
            "risk": "Low",
            "risk_score": 1
        },
        {
            "title": "Switch to Secondary Supplier",
            "description": "Alternative supplier with moderate cost and delivery time.",
            "cost": 8000,
            "delivery_days": 5,
            "risk": "Medium",
            "risk_score": 2
        },
        {
            "title": "Delay Product Launch",
            "description": "Avoid additional transportation cost but has higher business risk.",
            "cost": 0,
            "delivery_days": 14,
            "risk": "High",
            "risk_score": 3
        }
    ]

    # ---------------------------------------------------------
    # Generate 3 optimized alternatives
    # ---------------------------------------------------------

    objectives = [
        ("Fastest Delivery", 1.0, 0.1),
        ("Lowest Cost", 0.1, 1.0),
        ("Balanced Option", 0.5, 0.5)
    ]

    recommendations = []

    for objective_name, delivery_weight, cost_weight in objectives:

        # Objective:
        # minimize delivery time + cost
        objective = [
            delivery_weight * action["delivery_days"]
            + cost_weight * (action["cost"] / 10000)
            for action in actions
        ]

        # Constraint:
        # total selected action cost must be <= maximum budget
        budget_constraint = [
            action["cost"] for action in actions
        ]

        result = linprog(
            c=objective,
            A_ub=[budget_constraint],
            b_ub=[MAX_BUDGET],
            A_eq=[[1, 1, 1]],
            b_eq=[1],
            bounds=[(0, 1), (0, 1), (0, 1)],
            method="highs"
        )

        if result.success:

            selected_index = result.x.argmax()
            selected_action = actions[selected_index].copy()

            selected_action["optimization"] = objective_name

            recommendations.append(selected_action)

    return recommendations