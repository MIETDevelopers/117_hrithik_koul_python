'''Purpose:Create a child class Bus that will inherit all of the variables and
methods of the Vehicle class

Author:Hrithik Koul
'''
class Vehicle:
    vehicles_wheels=4
   
    def show_wheels(self):
        print(f"The vehicle has {self.vehicles_wheels} wheels")

class Bus(Vehicle):
    Company="Honda"
   
    def show_company(self):
        print(f"The Bus manufacturer company is {self.Company}")
       
       
b1=Bus()
b1.show_company()
b1.show_wheels()
