# Write a Python program to find intersection of two given arrays using Lambda.

list1 = []
list2 = []

n1 = int(input('Enter number of items: '))
for i in range(0,n1):
    num = int(input(f'Enter {i+1}th number: '))
    list1.append(num)

n2 = int(input('Enter number of items: '))
for i in range(0,n2):
    num = int(input(f'Enter {i+1}th number: '))
    list2.append(num)

result = list(filter(lambda x: x in list1, list2))
print(result)