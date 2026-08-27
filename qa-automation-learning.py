# Collect Tester Information

print("---------------------------------")
print("QA Test Execution System")
print("---------------------------------")

tester_name = input("Enter the Tester Name :: ")

browser = input("Browser you have used :: ")
browser = browser.lower().strip()

supported_browsers = ["chrome", "firefox", "edge"]
try:
    test_passed = input("Enter the Test Passed")
    test_passed=int(test_passed)
except ValueError:
    print("Enter a Valid Input")



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

if browser in supported_browsers:
    print("Supported Browser")
else:
    print("Unsupported Browser")


# Automation Environment Check

if browser in supported_browsers and len(test_cases) >= 5:
    print("You are ready for automation testing....")
else:
    print("Environment is not ready for automation testing")


# Reusable Test Function

def test_run(test_name):

    print(f"Executing test: {test_name}")

    if test_name == "Search" or test_name == "Checkout":
        return "FAIL"
    else:
        return "PASS"


# Execute Test Cases

for test in test_cases:

    result = test_run(test)

    print(f"Test Result: {result}")

    total_tests += 1

    if result == "PASS":
        passed_tests += 1
    else:
        failed_tests += 1


# Calculate Test Coverage

pass_percentage = (passed_tests / total_tests) * 100
failed_percentage = (failed_tests / total_tests) * 100


# Test Report

print("---------------------------------")
print("QA TEST REPORT")
print("---------------------------------")

print(f"Tester Name: {tester_name}")
print(f"Browser: {browser}")

print(f"Total Tests: {total_tests}")
print(f"Passed Tests: {passed_tests}")
print(f"Failed Tests: {failed_tests}")

print(f"Pass Percentage: {pass_percentage:.2f}%")
print(f"Fail Percentage: {failed_percentage:.2f}%")


# Coverage Decision

if total_tests >= 5:
    print("Good Test Coverage")
else:
    print("Add More Test Cases")

print("---------------------------------")