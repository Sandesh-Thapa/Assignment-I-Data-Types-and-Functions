# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

n = int(input('Enter range: '))
dict1 = dict()

for item in range(1, n+1):
    dict1[item] = item*item

print(dict1)