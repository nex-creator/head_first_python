def log_analyzer(logs: list):
    parsed_logs =[]
    level_count ={"INFO":0 ,"WARNING": 0, "ERROR":0}
    domain_users ={}
    for log in logs:
        timestamp, level,message, user_email = log.split("|")
        user_name , domain = user_email.strip().split("@")
        parsed_logs.append({
            "timestamp": timestamp.strip(),
            "level": level.strip(),
            "message": message.strip(),
            "user_name": user_name.strip(),
            "domain":domain.strip()
        })
    print(parsed_logs)
    for log in parsed_logs:
        level_count[log["level"]] +=1
        if log["domain"] in domain_users:
            domain_users[log["domain"]]["count"] +=1
            domain_users[log["domain"]]["user_name"].append(log["user_name"])
        else:
            domain_users[log["domain"]]={
                "count": 1,
                "user_name": [log["user_name"]]
            }


    print("Log level:")
    print(level_count)

    print("Domain_users:")
    print(domain_users)

        

logs = [
    "2026-01-21 10:10:00 | INFO | User logged in | alice@gmail.com",
    "2026-01-21 10:12:00 | ERROR | Payment failed | bob@yahoo.com",
    "2026-01-21 10:15:00 | INFO | Viewed dashboard | carol@gmail.com",
    "2026-01-21 10:20:00 | WARNING | Password attempt failed | alice@gmail.com",
    "2026-01-21 10:25:00 | INFO | User logged out | bob@yahoo.com",
]

log_analyzer(logs)