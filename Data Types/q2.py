# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

my_str = input('Enter String: ')

if len(my_str) > 2:
    result = my_str[:2] + my_str[-2:]
    print(result)
elif len(my_str) == 2:
    result = my_str + my_str
    print(result)
else:
    print('')

