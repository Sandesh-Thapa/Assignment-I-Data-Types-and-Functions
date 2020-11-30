# Write a Python program to print the even numbers from a given list

def even_list(list1):
    result = []
    for i in list1:
        if i % 2 == 0:
            result.append(i)
    return result

list = []
n = int(input('Enter number of items: '))

for i in range(0,n):
    num = int(input(f'Enter {i+1}th number: '))
    list.append(num)

print(even_list(list))
