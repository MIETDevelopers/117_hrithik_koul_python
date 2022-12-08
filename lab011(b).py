'''Purpose:Define class and instance attributes.

Author:Hrithik Koul
'''
class Cylinder:
    # class attribute
    pi = 3.14
    def __init__(self, radius, height):
    # instance variables
        self.radius = radius
        self.height = height
if __name__ == '__main__':
    c1 = Cylinder(4, 20)
    c2 = Cylinder(10, 50)
print(f'Value of Pi for cylinder c1 : {c1.pi} and cylinder c2 : {c2.pi}')
print(f'Radius of cylinder c1 : {c1.radius} and cylinder c2 : {c2.radius}')
print(f'Height of cylinder c1 : {c1.height} and cylinder c2 : {c2.height}')
print(f'Value of Pi for both cylinder c1 and c2 is : {Cylinder.pi}')