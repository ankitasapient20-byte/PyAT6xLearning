side1=float(input("Enter side 1: "))
side2=float(input("Enter side 2: "))
side3=float(input("Enter side 3: "))

def classify_triangle(a,b,c):
    if a>0 and b >0 and c>0:
        if a+b>c and a+c>b and b+c>a:
            if a==b==c:
                return "Equilateral"
            elif a==b or b==c or c==a:
                return "Isosceled"
            else:
                return "Scalene"

        else:
            print("Not a Triangle")

        result=classify_triangle(side1,side2,side3)
        print(f"the triange is classified as: {result}")
