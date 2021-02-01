# convert100.py
# A program to produce a table of Celsius temps to Fahrenheit conversions

def main():
    print("Temperature unit conversion table:")
    celsius = 0

    for i in range(11):
        fahrenheit = 9/5 * celsius + 32
        print("C =", celsius, " >> ", "F =", fahrenheit)
        celsius = celsius + 10


main()
