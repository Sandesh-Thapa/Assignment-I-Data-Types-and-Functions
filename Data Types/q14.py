#  Write a Python function to create the HTML string with tags around the word(s).

def add_tags(tag, content):
    result = f'<{tag}>{content}</{tag}>'
    return result

tag = input('Enter HTML tag: ')
content = input('Enter content: ')

print(add_tags(tag, content))