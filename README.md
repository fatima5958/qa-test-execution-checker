# QA Test Execution & Coverage Checker

## 📌 Project Overview

QA Test Execution & Coverage Checker is a beginner-level Python project that simulates a simple QA test execution system.

The program collects tester information, checks the automation environment, executes multiple test cases using a reusable function, and evaluates basic test coverage.

This project was created as part of my QA Automation and SDET learning journey.

## 🎯 Project Objectives

The main objectives of this project are to:

* Practice Python programming fundamentals
* Understand reusable functions
* Work with test case lists
* Use loops to execute multiple test cases
* Apply conditional logic
* Practice function parameters
* Perform basic test coverage checks
* Build a practical QA-focused Python project

## 🛠️ Technologies Used

* Python 3
* Git
* GitHub

## 🧠 Python Concepts Used

This project demonstrates the following Python concepts:

* Variables
* Data Types
* User Input
* Type Conversion
* `if / else`
* Comparison Operators
* `and / or`
* Lists
* List Indexing
* `len()`
* `for` Loops
* Functions
* Function Parameters
* f-Strings

## ⚙️ Features

### 1. Tester Information

The program collects:

* Tester name
* Browser name
* Number of passed test cases

### 2. Automation Environment Check

The program checks whether the environment is ready for automation testing.

The environment is considered ready when:

* The selected browser is Chrome
* At least 10 test cases have been passed

### 3. Test Case Management

The program maintains a list of test cases:

* Login
* Logout
* Add to Cart
* Search
* Checkout
* Profile

### 4. Automated Test Execution

Each test case is processed using a reusable Python function.

A `for` loop is used to execute all test cases without manually calling the function for every test.

### 5. Test Coverage Check

The program uses Python's `len()` function to calculate the total number of test cases.

It then evaluates whether the project has good basic test coverage.

## ▶️ How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/qa-test-execution-checker.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### Step 3: Navigate to the Project

```bash
cd qa-test-execution-checker
```

### Step 4: Run the Program

```bash
python qa_test_runner.py
```

## 📊 Example Output

```text
---------------------------------
QA Test Execution System
---------------------------------

Enter the Tester Name: Fatima
Enter the number of test cases passed: 10
Browser you have used: Chrome

You are ready for automation testing....

Executing test: Login
Login test executed successfully

Executing test: Logout
Test executed successfully

Executing test: Add to Cart
Test executed successfully

Executing test: Search
Test executed successfully

Executing test: Checkout
Test executed successfully

Executing test: Profile
Test executed successfully

Total Test Cases: 6
Passed Test Cases: 10

Good test coverage
```

## 📚 Learning Outcome

Through this project, I practiced using Python to build a small QA-focused test execution program.

The project helped me understand how programming fundamentals such as variables, conditions, lists, loops, functions, and parameters can be applied to a QA automation scenario.

This project is the first step in my roadmap toward becoming a QA Automation Engineer / SDET.

## 🚀 Future Improvements

Planned improvements for future versions include:

* Add failed test tracking
* Calculate test pass percentage
* Add input validation
* Add more test cases
* Add Pytest
* Create automated test reports
* Add API testing
* Add Selenium or Playwright automation
* Add CI/CD using GitHub Actions
* Add Docker support

## 📈 Learning Roadmap

This project is part of my larger QA Automation and SDET learning roadmap:

```text
Python
   ↓
Git & GitHub
   ↓
SQL
   ↓
Software Testing Fundamentals
   ↓
Pytest
   ↓
Selenium / Playwright
   ↓
API Testing
   ↓
Automation Frameworks
   ↓
CI/CD
   ↓
Docker & Linux
   ↓
SDET / Test Automation Architecture
   ↓
AI Automation
```

## 👨‍💻 Author

**Fatima**

QA Automation / SDET Learning Journey

---

⭐ This project is continuously being improved as I progress through my QA Automation and SDET learning journey.
