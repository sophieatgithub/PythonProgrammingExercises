# futvalperiods.py
# A program to compute the value of an investment
# carried 10 years into the future,
# interest calculated in periods

def main():
    print("This program calculates the future value")
    print("of an investment.")

    principal = eval(input("Enter the initial principal: "))
    years = eval(input("Enter the number of years invested: "))
    rate = eval(input("Enter the annual interest rate: "))
    periods = eval(input("Enter number of periods per year: "))
    evaluations = years * periods
    apr = rate/periods
    for i in range(evaluations):
        principal = principal * (1 + apr)

    print("The value in", years, "years is:", round(principal, 2))


main()

