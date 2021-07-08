# avgofnums.py
# A program which averages numbers entered by the user
# Input: number of numbers, numbers, Output: Average of numbers


def main():

    count = int(input("How many numbers do you want to average? "))
    total = 0

    for i in range(count):
        x = float(input("Enter number: "))
        total = total + x

    average = total / count
    print(average)


main()
