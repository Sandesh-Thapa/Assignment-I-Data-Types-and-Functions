# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).

my_str = input('Enter comma seperated words: ')

str_list = my_str.split(',')
str_list.sort()
print(str_list)