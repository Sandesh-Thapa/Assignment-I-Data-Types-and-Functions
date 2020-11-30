# Write a Python function that takes a list and returns a new list with unique elements of the first list

def unique_list(sampleList):
    unique = []
    
    for i in sampleList:
        if i not in unique:
            unique.append(i)
    return unique

list = []
n = int(input('Enter number of items: '))

for i in range(0,n):
    num = int(input(f'Enter {i+1}th number: '))
    list.append(num)

print(unique_list(list))
