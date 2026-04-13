from collections import defaultdict


def analyze_logs(logs):
    status = defaultdict(list)
    for log in logs:
        test_id = log.get("test_id")
        log_status = log.get("status")
        status[test_id].append(log_status)
    return status

def flaky_test(logs):
    test_records ={
        "flaky": [],
        "stable_pass": [],
        "stable_fail": [],
    }
    records = analyze_logs(logs)
    if not records:
        return test_records
    for test_id, statuses in records.items():
        status_set = set(statuses)
        print(status_set)
        if "PASS" in status_set and "FAIL" in status_set:
            test_records["flaky"].append(test_id)
        elif status_set == {"PASS"}:
            test_records["stable_pass"].append(test_id)
        elif status_set == {"FAIL"}:
            test_records["stable_fail"].append(test_id)
    return test_records



logs = [
    {"test_id": "T1", "status": "PASS"},
    {"test_id": "T2", "status": "FAIL"},
    {"test_id": "T1", "status": "FAIL"},
    {"test_id": "T3", "status": "PASS"},
    {"test_id": "T2", "status": "FAIL"},
    {"test_id": "T3", "status": "FAIL"},
]

print(analyze_logs(logs))
print(flaky_test(logs))