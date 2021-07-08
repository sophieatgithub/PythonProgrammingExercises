# sumofnums.py
# A program which sums numbers entered by the user
# Input: number of numbers, numbers, Output: sum of numbers

def main():

    count = int(input("How many numbers do you want to add together? "))
    total = 0

    for i in range(count):
        x = float(input("Enter number: "))
        total = total + x

    print(total)


main()
