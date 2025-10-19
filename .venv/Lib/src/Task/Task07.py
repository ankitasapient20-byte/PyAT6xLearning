#Write a program to checj whether the respose is sucessful
# (status code:200) or not

#response=404, failed API request
#response=200, Passed API request

StatusCode=int(input("Please enter the status code ro check the API response: ").strip())
if StatusCode==404:
    print("API req failed❌")
elif StatusCode==200:
    print("API status code OK✅️")
else:
    print("API status code NOT OK⚠️")