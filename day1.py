# tester_name="Fatima"
# tester_age=25
# experience_years=3.5
# is_automation_engineer=True
# test_case_completed=30
# print("Tester Name:", tester_name)
# print("Tester Age:", tester_age)
# print("Experience Years:", experience_years)
# print("Is Automation Engineer:", is_automation_engineer)
# print("Test Cases Completed:", test_case_completed)
# print(type(tester_name))
# print(type(tester_age))
# print(type(is_automation_engineer))
# print(type(test_case_completed))


# tester_name=input("Enter the Tester name ::")
# Browser_name=input("Enter the Browser name ::")
# test_cases= int(input("Test cases completed"))
# print(f"User {tester_name} has completed {test_cases} Test Cases in {Browser_name} Browser")


# test_cases=int(input("Enter number of passed test cases:"))
# if test_cases >= 10:
#     print("Test Execution PASSED")
# else:
#     print("Test Execution FAILED need improvement")


# expected_result = "PASS"
# actual_result = input("Enter actual result: ")
# if actual_result=="PASS":
#     print("PASSED")
# else:
#     print("FAILED")



# browser = input("Enter browser: ")
# test_cases = int(input("Enter completed test cases: "))

# if browser=="Chrome" and test_cases>=10:
#     print("Ready for automation testing")
# else:
#     print("Not ready for automation testing")


# test_cases=["Login" , "Logout" , "Search" , "Add to Cart" , "Checkout"]
# print(test_cases)
# print(test_cases[0])
# print(test_cases[2])
# print(test_cases[4])


# test_cases = ["Login", "Logout", "Search", "Add to Cart", "Checkout"]
# for test in test_cases:
#     print(f"Running Test : {test}") 


# test_cases = ["Login", "Logout", "Search", "Add to Cart", "Checkout"]
# length=len(test_cases)
# print(f"Number of test cases:: {length}")

# if length>=5:
#     print("Good test Coverge ")
# else:
#     print("Add more test cases")


# def run_test():
#     print("Runing Automation Test....")

# run_test()
# run_test()


def run_test(test_name):
    print(f"Runing automation Test :: {test_name}")

run_test("Login")
run_test("Search")
run_test("Checkout")