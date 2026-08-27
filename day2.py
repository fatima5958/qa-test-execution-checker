# Create a program that simulates 3 login attempts.

# attempt = 1
# while attempt <= 5:
#     print(f"Running Login test : {attempt} ")
#     if attempt == 3:
#         print("Login test Failed..Stopping execution")
#         break
#     attempt += 1


# tests = ["Login", "Logout", "Search", "Payment", "Checkout"]
#
# for test in tests:
#     if test == "Payment":
#         print(f"{test}Test is skipped")
#         continue
#     print(f"Running Test {test} ")


# def check_test(test_name):
#     if test_name == "Login":
#         return "PASS"
#     else:
#         return "FAIL"
#
# result = check_test ("Login")
# print(result)

# passed_tests=0
# failed_tests=0
# total_tests=0
#
# tests = ["Login", "Logout", "Search", "Checkout"]
# def check_test (test_name):
#     if test_name == "Login" or test_name== "Logout":
#         return "PASS"
#
#     else:
#         return "FAIL"
#
# for test in tests:
#     result = check_test(test)
#     print(f"{test} : {result}")
#     total_tests+=1
#     if result == "PASS":
#         passed_tests += 1
#     else:
#         failed_tests += 1
#
# print(f"Total Tests :: {total_tests}")
# print(f"Test Passed :: {passed_tests}")
# print(f"Failed Test :: {failed_tests} ")
#
# pass_percentage = (passed_tests / total_tests) * 100
# failed_percentage = (failed_tests / total_tests) * 100
#
# print(f"Percentage of Passed Tests {pass_percentage :.2f} ")
# print(f"Percentage of Failed Tests  {failed_percentage : .2f} ")

# try:
#     value = input("Enter the test_numbers :: ")
#     value =int(value)
#     print(f"Valid test case number : {value}")
# except ValueError:
#     print("Invalid test case number")

# supported_browsers = ["chrome", "firefox", "edge"]
# browser= input("Enter the browser name :: ")
# browser=browser.lower()
# browser=browser.strip()
# if browser in supported_browsers:
#     print("Supported browser")
# else:
#     print("Non_Supported Browser")

# test_results = {
#     "Login": "PASS",
#     "Logout": "PASS",
#     "Search": "FAIL",
#     "Checkout": "FAIL"
# }
# # print(test_results)
# print(test_results["Login"])
# print(test_results["Search"])
# for test,result in test_results.items():
#     print(f"{test}: {result}")
#     if result=="PASS":
#         print("Test Passed")
#     else:
#         print("Test Failed")

supported_browsers = ["chrome", "firefox", "edge"]
browser= input("Enter the name of the browser :: ")
browser=browser.lower().strip()
passed_tests=int(input("Enter the number of passed Test Cases :: "))

if browser in supported_browsers and passed_tests >= 10:
    print(f"{browser}+{passed_tests}")
    print("Environment Ready for Automation")
else:
    print(f"{browser}+{passed_tests}")
    print("Environment not Ready for Automation")

