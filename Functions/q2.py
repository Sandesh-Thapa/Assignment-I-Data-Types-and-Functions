# Write a Python function to sum all the numbers in a list.

def list_sum(list1):
    sum = 0
    for item in list1:
        sum += item
    return sum

list1 = []
n = int(input('Enter Number of Items: '))
for i in range(0,n):
    item = int(input(f'Enter {i+1}th item: '))
    list1.append(item)

print(list_sum(list1))