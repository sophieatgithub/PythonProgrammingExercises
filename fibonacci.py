# fibonacci.py
# A program to calculate the nth term of fibonacci


def main():

    n = int(input("Enter an integer for the nth term of fibonacci: "))
    previous = 0
    current = 1

    for i in range(n - 1):
        current, previous = current + previous, current

    print(current)


main()
