# Write a Python program to count the occurrences of each word in a given sentence

my_str = input('Enter Sentence: ')
word_list = my_str.split()
counts = dict()

for word in word_list:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)