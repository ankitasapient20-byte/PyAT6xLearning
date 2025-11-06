num1=int(input("Enter the first number\n "))
num2=int(input("Enter the second number\n "))
num3=int(input("Enter the third number\n"))

def sum_of_three(n1=100, n2=200, n3=300):
    return n1 + n2 + n3

result=sum_of_three(num1, num2, num3)
print(result)