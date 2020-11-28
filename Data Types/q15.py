# Write a Python function to insert a string in the middle of a string.

def insert_string_middle(wrapper,content):
    return wrapper[:2] + content + wrapper[2:]

wrapper = input('Enter Wrapper String: ')
content = input('Enter Content: ')

print(insert_string_middle(wrapper, content))
