# Write a Python program to filter a list of integers using Lambda.
list1 = []
n = int(input('Enter number of items: '))

for i in range(0,n):
    num = int(input(f'Enter {i+1}th number: '))
    list1.append(num)

even_list = list(filter(lambda i: i%2 == 0, list1))
print(even_list)