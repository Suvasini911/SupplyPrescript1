def get_recommendations(delay_risk):

    if delay_risk == 1:
        return [
            {
                "title": "Use Air Freight",
                "description": "Fastest delivery option to avoid shipment delay.",
                "cost": 15000,
                "delivery_days": 2,
                "risk": "Low"
            },
            {
                "title": "Switch to Secondary Supplier",
                "description": "Alternative supplier with slightly higher cost.",
                "cost": 8000,
                "delivery_days": 5,
                "risk": "Medium"
            },
            {
                "title": "Delay Product Launch",
                "description": "No transport cost but business impact is high.",
                "cost": 0,
                "delivery_days": 14,
                "risk": "High"
            }
        ]

    return [
        {
            "title": "Proceed Normally",
            "description": "Shipment is expected to arrive on time.",
            "cost": 0,
            "delivery_days": 0,
            "risk": "None"
        }
    ]