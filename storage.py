
issues = []
test_cases = []
# Stores issues and test cases while program is running

next_issue_id = 1
next_test_case_id = 1
# Keeps track of what ID to assign

def get_all_issues():
    return issues

def add_issue(issue):
    global next_issue_id
    issue["id"] = next_issue_id
    next_issue_id += 1
    issues.append(issue)
    # Assigns ID and increments the counter so the next issue gets a new ID
    # Stores the issue to issues

def get_all_test_cases():
    return test_cases

def add_test_case(test_case):
    global next_test_case_id
    test_case["id"] = next_test_case_id
    next_test_case_id += 1
    test_cases.append(test_case)

