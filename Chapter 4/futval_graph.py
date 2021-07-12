# futval_graph.py
# A program to draw a bar chart of return on investment over a 10 year period

from graphics import *

def main():

    print("Print bar chart of 10 year investment return.")

    principle = float(input("Enter principle investment: "))
    apr = float(input("Enter annual apr: "))

    win = GraphWin("Investment Growth Chart", 340, 240)

    Text(Point(20, 230), ' 0.0K').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80), ' 7.5K').draw(win)
    Text(Point(20, 30), ' 10.0K').draw(win)

    height = principle * 0.02
    bar1 = Rectangle(Point(40, 230), Point(65, 230 - height))
    bar1.draw(win)

    total = principle

    for i in range(1, 11):
        total = total * (1 + apr)
        xll = 25 * i + 40
        bar = Rectangle(Point(xll, 230), Point(xll + 25, 230 - total * 0.02))
        bar.draw(win)

    input("Press <Enter> to quit")
    win.close()


main()
