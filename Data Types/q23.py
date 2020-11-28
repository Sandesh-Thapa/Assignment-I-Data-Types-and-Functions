# Write a Python program to check a list is empty or not
list1 = []
n = int(input('Enter Number of Items: '))
for i in range(0,n):
    item = input(f'Enter {i+1}th item: ')
    list1.append(item)

if len(list1) == 0:
    print('Empty List')
else:
    print('Non-Empty List')