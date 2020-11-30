# Write a Python program to check whether a given string is number or not using Lambda

string_or_digit = lambda num: num.isdigit()

n = input('Enter value: ')
print(string_or_digit(n))