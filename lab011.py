'''Purpose:Write a python program that accepts the length of three sides of a triangle as inputs. The program 
should indicate whether or not the triangle is a right-angled triangle.(Use Pythagorean theorem) Also 
find out its area using Heron’s formula

Author:Hrithik Koul
'''
def area():
    a = float(input('Please Enter the First side of a Triangle: '))
    b = float(input('Please Enter the Second side of a Triangle: '))
    c = float(input('Please Enter the Third side of a Triangle: '))

    Perimeter = a + b + c

    s = (a + b + c) / 2
    
    Area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    
    print("The Perimeter of Traiangle = %.2f" %Perimeter);
    print("The Semi Perimeter of Traiangle = %.2f" %s);
    print("The Area of a Triangle is %0.2f" %Area)

def check():
    base=float(input("Enter length of Base : "))
    perp=float(input("Enter length of Perpendicular : "))
    hypo=float(input("Enter length of Hypotenuse : "))

    if hypo**2==((base**2)+(perp**2)):
        print("It's a right triangle")
    else:
        print("It's not a right triangle")

check()
area()