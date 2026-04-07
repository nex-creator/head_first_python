# def handle_records(records):
#     valid_records= []
#     for record in records:
#         vehicle_id = record.get("vehicle_id")
#         speed = record.get("speed")
#         if vehicle_id and speed is not None and speed >= 0:
#             valid_records.append(record)
#     return valid_records

# records = [
#     {"vehicle_id": "V1", "speed": 60},
#     {"vehicle_id": "V2", "speed": None},
#     {"vehicle_id": "", "speed": 50},
#     {"vehicle_id": "V3", "speed": -10},
# ]

# print(handle_records(records))





def grouping_records(records):
    grouped_record ={}
    for record in records:
        vehicle_id = record.get("vehicle_id")
        grouped_record[vehicle_id] = grouped_record.get(vehicle_id,0)+1
    return grouped_record


records_1 = [
    {"vehicle_id": "V1", "speed": 60},
    {"vehicle_id": "V1", "speed": 70},
    {"vehicle_id": "V2", "speed": 50},
    {"vehicle_id": "V1", "speed": 80},
    {"vehicle_id": "V2", "speed": 55},
]

print(grouping_records(records_1))