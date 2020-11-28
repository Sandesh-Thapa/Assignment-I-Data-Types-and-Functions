# Write a Python program to remove the nth index character from a nonempty string.

my_str = input('Enter a String: ')
n = int(input(f'Enter the index no to remove (0-{len(my_str)-1}): '))

if n <= len(my_str)-1:
    result = my_str[:n] + my_str[n+1:]
    print(result)
else:
    print('Outrageous Index Number !!!')

