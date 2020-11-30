# Write a Python function to multiply all the numbers in a list.

def list_product(list1):
    product = 1
    for item in list1:
        product *= item
    return product

list1 = []
n = int(input('Enter Number of Items: '))
for i in range(0,n):
    item = int(input(f'Enter {i+1}th item: '))
    list1.append(item)

print(list_product(list1))