# Write a Python program to remove an item from a tuple.

tup = ('I', 'N', 'S', 'I', 'G', 'H', 'T', 'W', 'O', 'R', 'K', 'S', 'H', 'O', 'P')

item = input('Enter item to remove: ')

list1 = list(tup) 
list1.remove(item) 
tup = tuple(list1)
print(tup)
