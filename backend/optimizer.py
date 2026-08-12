from scipy.optimize import linprog


MAX_BUDGET = 15000


def optimize_action(actions, objective):
    """Select one action using linear programming."""

    result = linprog(
        c=objective,
        A_ub=[[action["cost"] for action in actions]],
        b_ub=[MAX_BUDGET],
        A_eq=[[1, 1, 1]],
        b_eq=[1],
        bounds=[(0, 1)] * len(actions),
        method="highs"
    )

    if result.success:
        return actions[result.x.argmax()]

    return None


def get_recommendations(delay_risk):

    # If shipment is low risk
    if delay_risk == 0:
        return [
            {
                "title": "Proceed Normally",
                "description": "Shipment is expected to arrive on time.",
                "cost": 0,
                "delivery_days": 0,
                "risk": "None",
                "optimization": "Normal Operation"
            }
        ]

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
            "description": "Alternative supplier with a balanced cost and delivery time.",
            "cost": 8000,
            "delivery_days": 5,
            "risk": "Medium",
            "risk_score": 2
        },
        {
            "title": "Use Standard Shipping",
            "description": "Lower-cost option with a longer delivery time.",
            "cost": 3000,
            "delivery_days": 10,
            "risk": "High",
            "risk_score": 3
        }
    ]

    # 1. Fastest delivery
    fastest_objective = [
        action["delivery_days"]
        for action in actions
    ]

    # 2. Lowest cost
    lowest_cost_objective = [
        action["cost"]
        for action in actions
    ]

    # 3. Balanced cost + delivery
    balanced_objective = [
        (action["delivery_days"] / 10)
        + (action["cost"] / 15000)
        for action in actions
    ]

    objectives = [
        ("Fastest Delivery", fastest_objective),
        ("Lowest Cost", lowest_cost_objective),
        ("Balanced Option", balanced_objective)
    ]

    recommendations = []

    for optimization_name, objective in objectives:

        selected = optimize_action(actions, objective)

        if selected:
            recommendation = selected.copy()
            recommendation["optimization"] = optimization_name
            recommendations.append(recommendation)

    return recommendations