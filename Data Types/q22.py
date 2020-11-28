# Write a Python program to remove duplicates from a list.

list1 = []
result = []
n = int(input('Enter Number of Items: '))

for i in range(0,n):
    item = input(f'Enter {i+1}th item: ')
    list1.append(item)

for i in list1:
    if i not in result:
        result.append(i)

print(list(result))