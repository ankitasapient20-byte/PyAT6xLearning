#Grade Calculator
#Write a program that calculates and displays the letter grade for a given numerical score
#(e.g A,B,C,D or F)
#Based on the following grade scale

#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: 0-59

num=int(input("Enter a num\n"))
if num>=100 or num<=-1:
    print("You can't get a grade")
else:
if num>=90 and num<=100:
    print("Grade A")
elif num>=80 and num<=90:
    print("Grade B")
elif num>=70 and num<=80:
    print("Grade C")
elif num>=60 and num<=70:
    print("Grade D")
elif num>=50 and num<=60:
    print("Grade E")
