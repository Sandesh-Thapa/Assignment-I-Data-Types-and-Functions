# Write a Python function to find the Max of three numbers.

def max_num(x,y,z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z

x = int(input('Enter First number: '))
y = int(input('Enter Second number: '))
z = int(input('Enter Third number: '))

max = max_num(x,y,z)
print(max)