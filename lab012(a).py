'''Purpose:Defining instance variables using a constructor.

Author:Hrithik Koul
'''
class Dog:
    # Class Variable
    animal = 'Dog'
    # The init method or constructor
    def __init__(self, breed, color):
        # Instance Variable
        self.breed = breed
        self.color = color

# Objects of Dog class
Rodger = Dog("Pug", "Brown")
Buzo = Dog("Bulldog", "Black")
print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed :', Rodger.breed)
print('Color :', Rodger.color)
print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed :', Buzo.breed)
print('Color :', Buzo.color)
# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")

print(Dog.animal)