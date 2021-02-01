# futvalyearly.py
# A program to compute the value of an investment
# carried x years into the future, invested in yearly

def main():
    print("This program calculates the future value")
    print("of investments.")

    principal = eval(input("Enter the yearly investment: "))
    total = 0
    years = eval(input("Enter the number of years invested: "))
    apr = eval(input("Enter the annual interest rate: "))
    for i in range(years):
        total = (total + principal) * (1 + apr)
        if i == 0:
            print("The value in", i + 1, "year is:", round(total, 2))
        else:
            print("The value in", i + 1, "years is:", round(total, 2))


main()
