n = 100
print("This program illustrates a chaotic function")


def main():
    first = eval(input("Enter a number between 0 and 1: "))
    second = eval(input("Enter a second number between 0 and 1: "))

    for i in range(n):
        first = 3.9 * first * (1 - first)
        second = 3.9 * second * (1 - second)
        print(first, second)


main()
