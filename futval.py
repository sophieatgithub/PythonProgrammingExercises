# futval.py
# A program to compute the value of an investment
# carried x years into the future

def main():
    print("This program calculates the future value")
    print("of an investment.")

    principal = eval(input("Enter the initial principal: "))
    years = eval(input("Enter the number of years invested: "))
    apr = eval(input("Enter the annual interest rate: "))
    for i in range(years):
        principal = principal * (1 + apr)
        if i == 0:
            print("The value in", i + 1, "year is:", principal)
        else:
            print("The value in", i + 1, "years is:", principal)


main()
