# Write a Python program to sort a list of dictionaries using Lambda

person = [{'name':'John', 'age':18, 'address':'New York'}, {'name':'Jean', 'age':12, 'address':'Washington'}, {'name':'Smith', 'age':45, 'address':'Meryland'}]
sort_person = sorted(person, key = lambda x: x['age'])
print(sort_person)