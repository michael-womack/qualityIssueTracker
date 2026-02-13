
import storage

def create_issue(title, description, severity):
    issue = {
        "title": title,
        "description": description,
        "severity": severity,
        "status": "Open"
    }
    storage.add_issue(issue)
    # Creates a new issue and stores it

def list_issues():
    return storage.get_all_issues()
    # Returns all issues

def close_issue(issue_id):
    issues = storage.get_all_issues()
    for issue in issues:
        if issue["id"] == issue_id:
           issue["status"] = "Closed"
           return True
    return False
    # Marks an issue as closed

def create_test_case(issue_id, description):
    test_case = {
        "issue_id": issue_id,
        "description": description,
        "result": "Not Run"
    }
    storage.add_test_case(test_case)
    # Creates a test case linked to an issue

def list_test_cases(issue_id):
    results = []
    test_cases = storage.get_all_test_cases()
    for test_case in test_cases:
        if test_case["issue_id"] == issue_id:
            results.append(test_case)
    return results
    # Returns all test cases for an issue

def run_test_case(test_case_id, passed):
    test_cases = storage.get_all_test_cases()

    for test_case in test_cases:
        if test_case["id"] == test_case_id:
            if passed:
                test_case["result"] = "Passed"
            else:
                test_case["result"] = "Failed"
            return True
    return False
    # Sets the result of a test case (Pass/Fail)


