    
def analyze_logs(logs):
    parsed_logs = []

    for log in logs:
        timestamp, level, message, user_part = log.split("|")

        parsed_logs.append({
            "timestamp": timestamp.strip(),
            "level": level.strip(),
            "message": message.strip(),
            "user_id": int(user_part.strip().split("=")[1])
        })

    return parsed_logs

def generate_report(parsed_logs):
    level_count = {"INFO": 0, "ERROR": 0, "WARNING": 0}
    user_count = {}

    for log in parsed_logs:
        level_count[log["level"]] += 1
        user_id = log["user_id"]
        user_count[user_id] = user_count.get(user_id, 0) + 1

    most_active_user = max(user_count, key=user_count.get)

    print("Log Levels:")
    for level, count in level_count.items():
        print(f"{level}: {count}")

    print("\nMost Active User:")
    print(f"user_id={most_active_user} ({user_count[most_active_user]} actions)")



logs = [
    "2026-01-18 14:32:10 | INFO | User logged in | user_id=42",
    "2026-01-18 14:35:01 | ERROR | Payment failed | user_id=17",
    "2026-01-18 14:36:45 | INFO | Viewed dashboard | user_id=42",
    "2026-01-18 14:40:12 | WARNING | Password attempt failed | user_id=42",
    "2026-01-18 14:41:00 | INFO | User logged out | user_id=17",
]
parsed_logs = analyze_logs(logs)
generate_report(parsed_logs)