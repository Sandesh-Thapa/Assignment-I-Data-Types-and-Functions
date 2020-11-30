# Write a Python function to check whether a number is in a given range.

def is_range(num, initial, final):
    if num in range(initial, final):
        return True
    else:
        return False

numFrom = int(input('Enter initial range: '))
numTo = int(input('Enter final range: '))
n = int(input('Enter number to check: '))

print(is_range(n, numFrom, numTo))