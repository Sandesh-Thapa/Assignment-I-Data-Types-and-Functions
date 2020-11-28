# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

list = []
count = 0
n = int(input('Enter Number of Items: '))

for i in range(0,n):
    word = input(f'Enter {i+1}th item: ')
    list.append(word)
    if len(list[i]) >= 2 and list[i][0] == list[i][-1]:
        count += 1

print(count)
