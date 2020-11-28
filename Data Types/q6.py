# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.

my_str = input("Enter sentence: ")

if 'not' in my_str:
    if 'poor' in my_str:
        str_not = my_str.find('not')
        str_poor = my_str.find('poor')

        if str_poor > str_not:
            my_str = my_str.replace(my_str[str_not:(str_poor+4)], 'good')
            print(my_str)
        else:
            print(my_str) 
    else:
        print(my_str)
else:
    print(my_str)