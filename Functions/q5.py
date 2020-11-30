# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

def fact(n):
    if n == 0:
      return 1
    else:
        return n * fact(n-1)

num = int(input('Enter number to calculate factorial: '))
print(fact(num))