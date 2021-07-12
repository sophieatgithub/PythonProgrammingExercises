# graphicstest.py
# This is a program to test the graphics library graphics.py

from graphics import *


def main():

    win = GraphWin("Shapes")

    rect = Rectangle(Point(30, 30), Point(70, 70))
    rect.draw(win)

    win.getMouse()
    win.close()


main()
