# Write a Python program to get the largest number from a list.

list = []
largest = 0
n = int(input('Enter Number of Items: '))

for i in range(0,n):
    num = int(input(f'Enter {i+1}th number: '))
    list.append(num)
    if list[i] > largest:
        largest = list[i]

print(largest)