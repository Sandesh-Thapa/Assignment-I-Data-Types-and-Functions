# Write a Python program to multiplies all the items in a list.

list = []
product = 1
n = int(input('Enter Number of Items: '))

if n == 0:
    print('0')
else:
    for i in range(0,n):
        num = int(input(f'Enter {i+1}th number: '))
        product *= num
    print(product)