***TO-DO: 🔴 indicates an unfinished feature***


# Quality Issue Tracker

## Overview
This application is designed to model a simplified defect and deviation lifecycle, similar to processes used in regulated environments.
It emphasizes traceability, allowing users to manage issues and track their status.

---

## Features

### Issue Management
- Create quality issues or deviations with a title, description, and severity
- Track issue status (Open, Closed)
- List all existing issues with unique ID and details
- 🔴 Automatic timestamping for issue creation and closure (planned)
- 🔴 Filter issues by status or severity (planned)

### Test Case Management
- Add test cases linked to a specific issue
- Run test cases and record Pass/Fail results
- List all test cases
- 🔴 Automatic timestamping for test case execution (planned)

### User Interface
- Console-based interactive menu for all application functionality
- 🔴 GUI using Tkinter for a more user-friendly experience (planned)
  
---

## Tech Stack
- **Language:** Python
- **Storage:** In-memory lists. No database required.
- **UI:** 🔴 Tkinter (planned)

---

## Project Structure
```
- |- main.py            # Application entry point and menu
- |- actions.py         # Logic for issues and test cases
- |- storage.py         # In-memory storage for issues and test cases
- |- ui.py              # 🔴 Planned GUI using Tkinter
```
---

## How To Use

**1. Run the application**
- python main.py

**2. Follow the console menu to:**
- Create or list an issue
- Close an issue
- Add or run a test case
- List test cases for a given issue

**3. Example Workflow**
1. Create issue -> Enter title, description, severity
2. Add test case -> Link to issue by ID number
3. Run test case -> Record Pass/fail
4. Close issue -> Mark issue as resolved
