# Write a Python function that takes a list of words and returns the length of the longest one.

def longest_word_length(list1):
    longest = ''
    for word in list1:
        if len(word) > len(longest):
            longest = word 
    
    longest_length = len(longest)
    print(longest_length)


my_list = []
n = int(input('Enter number of words: '))

for i in range(0,n):
    word = input(f'Enter {i+1}th word: ')
    my_list.append(word)

longest_word_length(my_list)