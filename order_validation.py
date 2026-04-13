def order_validation(orders):
    records = {
        "valid_orders": [],
        'invalid_orders': [],
        "invalid_reasons": {}
    }
    for order in orders:
        id = order.get("order_id")
        amt = order.get("amount")
        status = order.get("status")
        reasons = []

        if id is None:
            reasons.append("Order id is missing.")

        if amt is None:
            reasons.append("Amount is missing")
        elif amt <= 0:
            reasons.append("Amount must be greater than 0")
        if status not in ["completed","pending"]:
            reasons.append("Invalid status")
        
        if reasons:
            records["invalid_orders"].append(id)
            records["invalid_reasons"][id] = reasons
        else:
            records["valid_orders"].append(id)
    return records


orders = [
    {"order_id": 1, "amount": 250, "status": "completed"},
    {"order_id": 2, "amount": -50, "status": "completed"},
    {"order_id": 3, "amount": 100, "status": "pending"},
    {"order_id": 4, "amount": 0, "status": "completed"},
    {"order_id": 5, "amount": -98, "status": "invalid"},
]

print(order_validation(orders))