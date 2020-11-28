# Write a Python program to clone or copy a list.

list1 = []
n = int(input('Enter Number of Items: '))
for i in range(0,n):
    item = input(f'Enter {i+1}th item: ')
    list1.append(item)

list2 = list(list1)
print(list2)