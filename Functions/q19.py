#  Write a Python program to create Fibonacci series upto n using Lambda.

from functools import reduce

fibo = lambda n: lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])

n = int(input('Enter number to calculate fibonaaci series: '))
print(fibo(n))