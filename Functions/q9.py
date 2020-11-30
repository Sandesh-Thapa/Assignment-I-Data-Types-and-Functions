#  Write a Python function that takes a number as a parameter and check the number is prime or not

def check_prime(num):
    if num == 0 or num == 1:
        print('Neither Prime Nor Composite !!!')
        return 0
    for i in range(2, num//2):
        if num % i == 0:
            return False
        else:
            return True

n = int(input('Enter Number to check prime: '))
print(check_prime(n))

