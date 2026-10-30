# QA Test Execution & Coverage Checker 🧪

A beginner-friendly **Python command-line learning project** for practicing test-case execution logic and QA reporting.

> **Scope:** This is a **simulation**, not a Selenium, browser, or API automation suite. It does not open a browser, interact with a live application, or measure real requirements coverage.

## What it demonstrates

- A predefined suite of six sample cases: Login, Logout, Add to Cart, Search, Checkout, Profile
- Basic browser-name validation (Chrome, Firefox, Edge)
- A reusable function returning simulated `PASS`/`FAIL` outcomes
- Total executed, passed, and failed counts
- Pass/fail percentages printed as a console report
- A simple case-count-based “coverage” indicator

The results are deliberately hard-coded for demonstration: **Search** and **Checkout** fail; the other four pass.

## Requirements

- Python 3 (standard library only; no external packages)

## Run it

Clone the repository or download the files, then run the main exercise:

```bash
python qa-automation-learning.py
```

Enter a tester name and a browser name when prompted. On some systems the command is `python3` instead of `python`.

### Expected report for a supported browser

```text
Total Tests: 6
Passed Tests: 4
Failed Tests: 2
Pass Percentage: 66.67%
Fail Percentage: 33.33%
Test Coverage Status: Good Test Coverage
```

The “coverage” label uses **five or more listed cases** as a learning rule. It is **not** code coverage, path coverage, or requirements traceability.

## Files

| File | Purpose |
| --- | --- |
| [`qa-automation-learning.py`](./qa-automation-learning.py) | Main simulated execution and report |
| [`project1.py`](./project1.py) | Earlier interactive QA practice exercise |
| [`day1.py`](./day1.py) | Python functions and basic testing exercises |
| [`day2.py`](./day2.py) | Conditions, browsers, and test-result practice |

## Ideas for the next iteration

- Replace simulated outcomes with real assertions using `pytest`
- Add API tests with mocked services or a safe public test API
- Export structured test results and introduce proper coverage mapping
- Add automated checks in GitHub Actions

**Author:** [Mateen Fatima](https://github.com/fatima5958) · BS Software Engineering (2026)
