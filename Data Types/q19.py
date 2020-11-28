# Write a Python program to get the smallest number from a list.

list = []
n = int(input('Enter Number of Items: '))

for i in range(0,n):
    num = int(input(f'Enter {i+1}th number: '))
    list.append(num)

print(min(list))