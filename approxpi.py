# approxpi.py
# A program to approximate pi using a sequence, to n terms
# input: number of terms, output: approximation of pi, pi - approx
import math


def main():

    n = int(input("Enter number of terms: "))
    total = 4

    while n > 1:

        denominator = n * 2 - 1
        if n % 2 == 0:
            total = total - 4 / denominator
        else:
            total = total + 4 / denominator
        n = n - 1

    difference = math.pi - total
    print(total)
    print(difference, "off from math.pi")


main()
