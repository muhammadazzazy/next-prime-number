from sympy import isprime
from sys import exit


def main() -> None:
    count: int = 1
    exit_message: str = 'Exiting program...'
    while True:
        try:
            choice = input('Do you want the next prime number? (Y/n) ')
        except KeyboardInterrupt:
            print(exit_message)
        if choice.lower() == 'y':
            while not isprime(count):
                count += 1
            print(f'{count} is the next prime number!')
            count += 1
        else:
            print(exit_message)
            exit()


if __name__ == '__main__':
    main()
