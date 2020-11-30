#  Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def check_string(string):
    countUpper = 0
    countLower = 0

    for letter in string:
        if letter.isupper():
            countUpper += 1
        elif letter.islower():
            countLower += 1
    print(f'No. of Upper case Characters: {countUpper}')
    print(f'No. of Lower case Characters: {countLower}')
    
str1 = input('Enter String:')
print(check_string(str1))