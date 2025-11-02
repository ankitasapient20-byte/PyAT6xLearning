num= int(input("Enter a number: "))
#5
fact=1
if num<0:
    print("Fact is not defined!")
    if num==0:
        print("Fact = ",fact)
else:
    for i in range(1,num+1): #1,2,3,4,5
 fact= fact * i
print("Factorial of : ",fact)