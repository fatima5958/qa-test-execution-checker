# Collect Tester Information
print("---------------------------------")
print("QA Test Execution System")
print("---------------------------------")

tester_name=input("Enter the Tester Name :: ")
test_passed=int(input("Enter the number of test cases passed :: "))
browser=input("Browser you have use :: ")

#Define Test cases

test_cases=["Login" ,"Logout" ,"Add to Cart" ,"Search" ,"Checkout" ,"Profile" ] 

if browser=="Chrome" and test_passed >=10:
    print("You are ready for automation testing....")
else:
    print("Environment is not ready for automation testing")

# Crete Reuseable Test Function

def test_run(test_name):
    print(f"Executing test: {test_name}")
    if test_name=="Login":
        print("Hey Login is Successful")
    else:
        print("Excection passed...")

for test in test_cases:
 test_run(test)

# Check the Coverge

length=len(test_cases)
print(f"Total Test Cases :: {length}")
print(f"Passed test cases :: {test_passed}")


# Coverage Decision
if length>=5:
    print("Good test coverge")
else:
    print("Bad Test Coverge")





