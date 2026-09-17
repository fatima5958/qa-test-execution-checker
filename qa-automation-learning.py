# QA Test Execution & Coverage Checker

print("---------------------------------")
print("QA Test Execution & Coverage Checker")
print("---------------------------------")

# Collect Tester Information
tester_name = input("Enter Tester Name: ").strip()

browser = input("Enter Browser (Chrome/Firefox/Edge): ").lower().strip()

supported_browsers = ["chrome", "firefox", "edge"]

# Counters
passed_tests = 0
failed_tests = 0
total_tests = 0

# Define Test Cases
test_cases = [
    "Login",
    "Logout",
    "Add to Cart",
    "Search",
    "Checkout",
    "Profile"
]

# Browser Check
print("\n--- Browser Check ---")

if browser in supported_browsers:
    print(f"Browser: {browser.title()}")
    print("Status: Supported")
else:
    print(f"Browser: {browser}")
    print("Status: Unsupported")

# Automation Environment Check
print("\n--- Automation Environment Check ---")

if browser in supported_browsers and len(test_cases) >= 5:
    print("Environment Status: Ready for automation testing")
else:
    print("Environment Status: Not ready for automation testing")

# Reusable Test Function
def test_run(test_name):
    print(f"Executing test: {test_name}")

    # Simulated test results for this learning project
    if test_name in ["Search", "Checkout"]:
        return "FAIL"
    else:
        return "PASS"


# Execute Test Cases
print("\n--- Test Execution ---")

for test in test_cases:

    result = test_run(test)

    print(f"Test Result: {result}")
    print("---------------------------------")

    total_tests += 1

    if result == "PASS":
        passed_tests += 1
    else:
        failed_tests += 1


# Calculate Test Results
if total_tests > 0:
    pass_percentage = (passed_tests / total_tests) * 100
    fail_percentage = (failed_tests / total_tests) * 100
else:
    pass_percentage = 0
    fail_percentage = 0


# Test Report
print("\n---------------------------------")
print("QA TEST REPORT")
print("---------------------------------")

print(f"Tester Name: {tester_name}")
print(f"Browser: {browser.title()}")

print(f"Total Tests: {total_tests}")
print(f"Passed Tests: {passed_tests}")
print(f"Failed Tests: {failed_tests}")

print(f"Pass Percentage: {pass_percentage:.2f}%")
print(f"Fail Percentage: {fail_percentage:.2f}%")

# Coverage Decision
print("\n--- Test Coverage ---")

if total_tests >= 5:
    print("Test Coverage Status: Good Test Coverage")
else:
    print("Test Coverage Status: Add More Test Cases")

print("---------------------------------")
print("Test execution completed.")
print("---------------------------------")
