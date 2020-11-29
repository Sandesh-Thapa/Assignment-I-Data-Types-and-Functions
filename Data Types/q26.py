# Write a Python program to insert a given string at the beginning of all items in a list

list1 = []
n = int(input('Enter Number of Items: '))
for i in range(0,n):
    item = input(f'Enter {i+1}th item: ')
    list1.append(item)

string = input('Enter String: ')

# for i in list1:
#     print(['{}{}'.format(string,i)])   => returns ['{string}1][{string}2]...[{string}N]

print(['{0}{1}'.format(string,i) for i in  list1])