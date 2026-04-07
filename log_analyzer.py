from collections import defaultdict


def log_analyzer(logs):
    total_test_status = {}
    for log in logs:
        status = log.get("status")
        if status:
            total_test_status[status] = total_test_status.get(status,0) + 1
    return total_test_status

def error_analyzer(logs):
    error_type = defaultdict(list)
    for log in logs:
        error = log.get("error")
        test_id = log.get("test_id")
        if log.get("status") == "FAIL" and error is not None:
            error_type[error].append(test_id)
    return error_type

def most_common_failure(logs):
    failures = error_analyzer(logs) # here failures is a dict which contains lists
    most_common_error = None
    max_count = 0
    for failure,value in failures.items():
        count = len(value)
        if count > max_count:
            max_count = count
            most_common_error = failure
    return most_common_error

logs = [
    {"test_id": "T1", "status": "FAIL", "error": "Timeout"},
    {"test_id": "T2", "status": "PASS", "error": None},
    {"test_id": "T3", "status": "FAIL", "error": "ElementNotFound"},
    {"test_id": "T4", "status": "FAIL", "error": "Timeout"},
    {"test_id": "T5", "status": "PASS", "error": None},
]
print(log_analyzer(logs))
print(error_analyzer(logs))
print(most_common_failure(logs))