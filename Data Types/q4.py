# . Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

str1 = input('Enter String1: ')
str2 = input('Enter String2: ')

result = str2[:2] + str1[2:] + ' ' + str1[:2] + str2[2:]

print(result)