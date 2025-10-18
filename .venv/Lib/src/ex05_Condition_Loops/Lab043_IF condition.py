#Write a program to take user age and
#let hom know if he can go to club or not
#21

#logic bulding formula

#Step-1
#i/p- age, int
#o/p- String

#Step-2 roungh lofic (brute force)
#age>21 [rint(can fo to club)
#age<21 print(can't go to clib)

#Step03 Write the logic
age=int(input("Eneter the age\n").strip()) #Remove whitespaces
if age<=0 or age>130:
    print("Enter a valid age")
else:
    print("Can go to club")
    if age>=21:
        print("You cango  to club")
    else:
        print("You can't go to club")

#Check for edge cases
#Optimize the code
