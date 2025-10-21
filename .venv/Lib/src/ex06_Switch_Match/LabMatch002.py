

print("enter which test you want to run")
test_type=input("Enter test type: APT, UI, Performance, Security:  ")
match test_type:
    case "API":
        print("We're running a POSTMAn API testcase")
    case "UI":
        print("We're running selenium testcase")
    case "Performance":
        print("We're running a Performance testcase")
    case "Security":
        print("We're running security testcase")
    case _:
        print("Invalid Input")