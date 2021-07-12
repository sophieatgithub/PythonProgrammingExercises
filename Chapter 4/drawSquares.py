# drawSquares.py
# A program to draw 10 squares to the window, where clicked

from graphics import *

def main():

    win = GraphWin()
    shape = Rectangle(Point(0, 0), Point(50, 50))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    for i in range(10):

        p = win.getMouse()
        newshape = shape.clone()
        newshape.move(p.getX() - 25, p.getY() - 25)
        newshape.draw(win)

        print("Click again to quit.")

    win.close()


main()
