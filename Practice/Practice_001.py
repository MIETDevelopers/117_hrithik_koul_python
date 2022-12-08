'''Purpose:Write a Python program to create a Vehicle class
with max_speed and mileage instance attributes.

Author:Hrithik Koul
'''
class Vehicle:
    def __init__(self,speed,mileage):
        self.max_speed=speed
        self.mileage=mileage

    def show(self):
        print(f"The max_speed of car is {self.max_speed}")
        print(f"The mileage of car is {self.mileage}")
       
v1=Vehicle(30,30)
v1.show()