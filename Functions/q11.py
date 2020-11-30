#  Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result.

add = lambda num: num+15
mul = lambda x, y: x*y

a = int(input('Enter Number to add: '))
print(add(a))

x = int(input('Enter First number to multiply: '))
y = int(input('Enter Second number to multiply: '))
print(mul(x, y))