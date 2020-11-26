# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

my_str = input('Enter String: ')
n = len(my_str)
first_char = my_str[0]
result = ''

for i in range(1,n):
    if my_str[i] == first_char:
        result += '$'
    else:
        result += my_str[i]

print(first_char + result)




