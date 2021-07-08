# volandsaofsphere
# Calculating the volume and surface area of a sphere
# Input: radius, output: volume and surface area

import math


def main():

    radius = float(input("Enter radius: "))
    volume = (4/3) * math.pi * (radius**3)
    area = 4 * math.pi * (radius**2)

    print("Volume: ", volume)
    print("Area: ", area)


main()
