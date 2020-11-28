# Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

my_str = input('Enter a string: ')
print(my_str[-1] + my_str[1:-1] + my_str[0])