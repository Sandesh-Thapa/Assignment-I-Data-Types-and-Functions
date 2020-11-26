# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

my_str = input('Enter a string: ')
result = ''

if len(my_str) >= 3:
    if my_str[-3:] == 'ing':
        result = my_str + 'ly'
        print(result)
    else:
        result = my_str + 'ing'
        print(result)
else:
    print(my_str)

