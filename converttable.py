# converttable.py
# A program to displat the convertions of Celsius to Fahrenheit
# for every 10 digits from 10 to 100, display the fahrenheit equivalent
#         fahrenheit = 9/5 * celsius + 32
#

def main():

    print("C", end=" | ")
    print("F")
    print("--------")

    for cel in range(0, 100, 10):
        fah = 9/5 * cel + 32
        print(cel, end=" | ")
        print(fah)
        print("--------")


main()
