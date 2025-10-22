'''In automation, you often compare expected and actual outputs.
Write code to check if a test case passed or failed.

expected_title = "Dashboard"
actual_title = "Dashboard "

✅ Test Passed – Title matches'''
expected_title = input("Expected title: ".strip())
actual_title = input("Actual title: ".strip())
if expected_title.lower() == actual_title or actual_title.lower() == expected_title:
    print("Passed✅")
elif(expected_title == actual_title):
    print("Passed✅")
else:
    print("Failed❌")
