# Write a Python program to square and cube every number in a given list of integers using Lambda.

list1 = []
n = int(input('Enter number of items: '))

for i in range(0,n):
    num = int(input(f'Enter {i+1}th number: '))
    list1.append(num)

square_list = list(map(lambda i: i ** 2, list1))
cube_list = list(map(lambda i: i ** 3, list1))