# Write a Python program to sort a list of tuples using Lambda.

tup = [('John', 32), ('Jean', 18), ('Smith', 45)]
tup.sort(key = lambda x: x[1])
print(tup)
