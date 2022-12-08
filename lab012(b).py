'''Purpose:Defining instance variables using the normal method.

Author:Hrithik Koul
'''
class Dog:
# Class Variable
    animal = 'Dog'
    # The init method or constructor
    def __init__(self, breed):
        # Instance Variable
        self.breed = breed
    # Adds an instance variable
    def setColor(self, color):
        self.color = color
    # Retrieves instance variable
    def getColor(self):
        return self.color

# Driver Code
Rodger = Dog("Pug")
Rodger.setColor("Brown")
print(Rodger.getColor())