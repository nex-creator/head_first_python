from collections import defaultdict


def analyze_logs(logs):
    grouped_test_id = defaultdict(list)
    for log in logs:
        test_id = log.get("test_id")
        status = log.get("status")
        timestamp = log.get("timestamp")
        if test_id and status and timestamp is not None:
            grouped_test_id[test_id].append((status,timestamp))
        for test_id in grouped_test_id:
            grouped_test_id[test_id].sort(key=lambda x: x[1])
    return grouped_test_id


def analyze_test_behavior(logs):
    records = analyze_logs(logs)
    result ={
        "flaky": [],
        "intermittent": [],
        "stable_pass":[],
        "stable_fail":[],
    }
    for test_id, values in records.items():
        statuses = [status for status, _  in values]
        #to check flakiness
        status_set = set(statuses)
        if "PASS" in status_set and "FAIL" in status_set:
            result["flaky"].append(test_id)
        elif status_set == {"PASS"}:
            result["stable_pass"].append(test_id)
        elif status_set == {"FAIL"}:
            result["stable_fail"].append(test_id)
        for i in range(len(statuses)-1):
            if statuses[i] == "FAIL" and statuses[i+1] == "PASS":
                result["intermittent"].append(test_id)
    return result

        





logs = [
    {"test_id": "T1", "status": "PASS", "timestamp": 1},
    {"test_id": "T1", "status": "FAIL", "timestamp": 3},
    {"test_id": "T1", "status": "PASS", "timestamp": 2},

    {"test_id": "T2", "status": "FAIL", "timestamp": 1},
    {"test_id": "T2", "status": "FAIL", "timestamp": 2},

    {"test_id": "T3", "status": "PASS", "timestamp": 1},
    {"test_id": "T3", "status": "PASS", "timestamp": 2},

    {"test_id": "T4", "status": "FAIL", "timestamp": 1},
    {"test_id": "T4", "status": "PASS", "timestamp": 2},
]

print(analyze_logs(logs))
print(analyze_test_behavior(logs))