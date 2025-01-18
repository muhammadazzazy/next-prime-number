from sympy import isprime

count = 1
while True:
    choice = input('Do you want the next prime number? (Y/n) ')
    if choice.lower() == 'y':
        while not isprime(count):
            count += 1
        print(f'{count} is the next prime number!')
        count += 1
    else:
        quit()
