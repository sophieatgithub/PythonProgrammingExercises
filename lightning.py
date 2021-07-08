# lightning.py
# A program to calculate the distance to lightning
# input: time between lightning and thunder in seconds, output: distance in meters
# speed of sound ~ 343 m/s
# distance = speed * time

def main():

    time = int(input("Enter time in seconds: "))

    distance = 343 * time

    print(distance, " meters away.")


main()
