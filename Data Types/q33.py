# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys

dict1 = dict()

for item in range(1, 16):
    dict1[item] = item*item

print(dict1)