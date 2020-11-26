# Write a Python program to count the number of characters (character frequency) 

my_str = input('Enter String: ')
my_dict = {}

for key in my_str:
    keys = my_dict.keys()
    if key in keys:
        my_dict[key] += 1
    else:
        my_dict[key] = 1

print(my_dict)

