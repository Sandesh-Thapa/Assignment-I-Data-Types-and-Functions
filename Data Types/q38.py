# Write a Python program to remove a key from a dictionary.

dict1 = {'a':1,'b':2,'c':3,'d':4}
key = input('Enter key to remove: ')

if key in dict1: 
    del dict1[key]
else:
    print(f"key {key} doesn't exists")
