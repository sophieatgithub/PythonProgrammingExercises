# pizza.py
# Program to calculate the cost per a square inch of pizza
# input: diameter and cost of pizza, output: cost per square inch
# 1. input diameter and cost, 2. calculate radius, 3. calculate surface area
# 4. calculate cost/surface area, 5. print cost/square inch
import math


def main():
    cost, diameter = eval(input("Enter: cost, diameter: "))

    radius = diameter / 2
    area = math.pi * (radius**2)
    costperinch = round((cost / area), 2)

    print("£/inch", costperinch)


main()
