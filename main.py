
import actions

def show_menu():
    print("\n\033[1;36mQuality Issue Tracker\033[0m\n")
    print("1. Create issue")
    print("2. List issues")
    print("3. Close issue")
    print("4. Add test case")
    print("5. List test cases for an issue")
    print("6. Run test case")
    print("7. Exit")
    # Main menu for the application

def create_issue_flow():
    title = input("Enter new issue title: ")
    description = input("Enter issue description: ")
    severity = input("Enter severity (Low / Medium / High): ")

    actions.create_issue(title,description,severity)
    print("New issue created.")

def list_issues_flow():
    issues = actions.list_issues()

    if not issues:
        print("No issues found.")
        return

    for issue in issues:
        print(
            "ID:", issue["id"],
            "| Title:", issue["title"],
            "| Severity:", issue["severity"],
            "| Status:", issue["status"],
        )

def close_issue_flow():
    issue_id = int(input("Enter issue ID to close: "))
    success = actions.close_issue(issue_id)

    if success:
        print("Issue closed.")
    else:
        print("Issue not found.")

def add_test_case_flow():
    issue_id = int(input("Enter issue ID: "))
    description = input("Enter test case description: ")

    actions.create_test_case(issue_id, description)
    print("Test case added.")

def list_test_cases_flow():
    issue_id = int(input("Enter issue ID: "))
    test_cases = actions.list_test_cases(issue_id)

    if not test_cases:
        print("No test cases found.")
        return

    for test_case in test_cases:
        print(
            "ID:", test_case["id"],
            "| Description:", test_case["description"],
            "| Result:", test_case["result"]
        )

def run_test_case_flow():
    test_case_id = int(input("Enter test case ID: "))
    result = input("Did the test pass? (y/n): ")

    passed = result.lower() == "y"
    success = actions.run_test_case(test_case_id, passed)

    if success:
        print("Test case updated.")
    else:
        print("Test case not found.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            create_issue_flow()
        elif choice == "2":
            list_issues_flow()
        elif choice == "3":
            close_issue_flow()
        elif choice == "4":
            add_test_case_flow()
        elif choice == "5":
            list_test_cases_flow()
        elif choice == "6":
            run_test_case_flow()
        elif choice == "7":
            print("Application Closed.")
        else:
            print("Invalid option. Please try again.")

main()
