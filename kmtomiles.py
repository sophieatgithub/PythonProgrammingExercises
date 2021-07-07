# kmtomiles.py
# Problem: have a distance in km but need to know it in miles
# Solution: A program to convert km to miles
# Specifications: input number of km, output the distance in miles
# Design: 1. prompt user for a number of km. 2. convert number of km to miles 3. print number of miles to screen
# Implement design:

def main():
    km = eval(input("Enter number of kilometers: "))
    miles = km * 0.62
    print(km, "km is", miles, "miles.")


main()
