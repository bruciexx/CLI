#!/usr/bin/env python
def is_prime(num):
    if num <= 1:
        return "not prime"
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                return "not prime"
            else:
                continue
        return "prime"

while True:
    try:
        try:
            n = input("Enter an integer:\n>")
            print(n, "is", is_prime(int(n)))
        except ValueError:
            if n == '':
                continue
            elif n == 'exit' or n == 'quit' or n == "q":
                exit(0)
            elif n == 'c' or n == 'clear':
                print('\033c', end='')
                continue
            else:
                print("That was not an integer please try again or type 'exit' to exit the program")
                continue
    except KeyboardInterrupt:
        print("\033c", end="")
        print("Goodbye!")
        exit(0)
