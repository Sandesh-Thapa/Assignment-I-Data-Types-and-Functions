# Write a Python program to remove the characters which have odd index values of a given string.

my_str = input('Enter a string: ')
result = ''
for i in range(len(my_str)):
    if i%2 == 0:
        result += my_str[i]
    
print(result)

