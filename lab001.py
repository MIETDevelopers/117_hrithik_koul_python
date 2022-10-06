'''Purpose:Write a program to demonstrate type checking of various data types and demonstrate the use of following built in functions in python: abs(), len(), min(), round(), isalnum(), type().

Author:Hrithik Koul
'''
a=12
print(type(a))

a=12.22
print(type(a))

a="hello"
print(type(a))

a="1+2j"
print(type(a))

a=-12
print(abs(a))

a=[1,2,3]
print(len(a))

a=12
b=13
print(max(a,b))

a=12
b=13
print(min(a,b))

a=13.6
print(round(a))

a="hello1"
print(a.isalnum())

