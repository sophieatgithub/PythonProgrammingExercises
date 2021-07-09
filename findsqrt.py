# findsqrt.py
# A program to guess the square root
# input: a number to sqrt, iterations output: best guess, maths.sqrt - best guess
import math

def main():

    x = float(input("Enter number to square root: "))
    iterations = int(input("Enter iterations: "))

    guess = x / 2

    for i in range(iterations):
        guess = (guess + (x / guess)) / 2

    print("The guess is: ", guess)
    print("Difference from math.sqrt: ", math.sqrt(x) - guess)


main()
