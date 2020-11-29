# Write a Python program to replace the last element in a list with another list.

list1 = []
list2 = []

n1 = int(input('Enter number of items for first list: '))
for i in range(0,n1):
    item = input(f'Enter {i+1}th item: ')
    list1.append(item)

n2 = int(input('Enter number of items for first second list: '))
for i in range(0,n2):
    item = input(f'Enter {i+1}th item: ')
    list2.append(item)

list1[-1:] = list2
print(list1)