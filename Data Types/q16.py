# Write a Python program to sum all the items in a list.

list = []
sum = 0
n = int(input('Enter Number of Items: '))

for i in range(0,n):
    num = int(input(f'Enter {i+1}th number: '))
    sum += num

print(sum)