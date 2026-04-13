# from collections import defaultdict


def api_response_validator(responses):
    records ={
        "valid":[],
        "invalid":[],
        "invalid_reasons": {}
    }
    for response in responses:
        name = response.get("name")
        age = response.get("age")
        status = response.get("status")
        user_id = response.get("id")
        reasons = []

        if not name:
            reasons.append("Name is empty")   
        if age is None:
            reasons.append("Age is missing")
        elif age < 0 or age >120:
            reasons.append("Age out of valid range")

        if status not in ["active","inactive"]:
            reasons.append("Invalid status")

        if reasons:
            records['invalid'].append(user_id)
            records["invalid_reasons"][user_id] = reasons
        else:
            records["valid"].append(user_id)
    return records



response = [
    {"id": 1, "name": "Alice", "status": "active", "age": 25},
    {"id": 2, "name": "Bob", "status": "inactive", "age": 17},
    {"id": 3, "name": "", "status": "active", "age": 30},
    {"id": 4, "name": "David", "status": "active", "age": -5},
    {"id": 5, "name": "Eva", "status": "active", "age": 40},
]

print(api_response_validator(response))