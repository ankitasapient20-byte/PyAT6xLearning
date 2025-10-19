#Find the Max between 3 numbers

#Logic building
#User i/p- num1,num2,num3-->int
#o/p- int or str with max number

num1=int(input("Enter a num1\n"))
num2=int(input("Enter a num2\n"))
num3=int(input("Enter a num3\n"))

#num1>num2 and num1>num3 (num1 is max)
#num2>num1 and num2>num3 (num2 is max)
#else num3 is max

if num1>num2 and num1>num3:
    print(num1)
elif num2>num3 and num2>num1:
    print(num2)
else:
    print(num3)

