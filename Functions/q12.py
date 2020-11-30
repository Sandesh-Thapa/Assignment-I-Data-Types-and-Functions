# Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.

def mul(n):
    def product():
        return n * 10
    return mul

n = int(input('Enter number: '))
print(mul(n))
