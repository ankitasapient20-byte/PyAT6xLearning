'''You want to check whether a web page loads within 3 seconds (performance test condition).

load_time = 4.2
⚠️ Page load too slow: 4.2 seconds'''

web_page = input(r"Enter the Web url: ")
load_time = float(input("Enter the load time in seconds: "))
if load_time<4.2:
    print("web page loads within 3 seconds➡️")
elif load_time==4.2:
    print("web page load too slow: 4.2 seconds⚠️")
else:
    print("invalid input")