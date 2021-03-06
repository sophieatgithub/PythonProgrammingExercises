# A program which converts celsius to fahrenheit

def main():
    print("This program converts celsius to fahrenheit")

    celsius = eval(input("Enter temperature in celsius: "))
    fahrenheit = (celsius * 1.8) + 32

    print(celsius, "celsius, is", round(fahrenheit, 1), "fahrenheit.")


main()
