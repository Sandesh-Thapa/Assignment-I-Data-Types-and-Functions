#  Write a Python program to convert a list to a tuple.

list1 = []
n = int(input('Enter Number of Items: '))
for i in range(0,n):
    item = input(f'Enter {i+1}th item: ')
    list1.append(item)

tup = tuple(list1)
print(tup)
