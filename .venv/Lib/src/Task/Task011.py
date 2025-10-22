'''Given a Number a number you need to calculate the factorial of that number
n = 5
Fact = 5×4×3*2*1 = 120
Fact = 0 → 1, '''
n=int(input("Enter a number: "))
if n < 0:
 print("Factorial is not defined for negative numbers.")
elif n == 0 or n == 1:
    print(1)
else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        print("factorial of given no. is: ",factorial)



