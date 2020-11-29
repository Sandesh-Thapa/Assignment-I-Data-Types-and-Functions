# Write a Python program to multiply all the items in a dictionary.

dict1 = {1: 10, 2: 20, 3: 30}

product = 1
for key in dict1:    
    product=product * dict1[key]

print(product)