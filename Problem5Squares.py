# Symone Mitchell
# August 23, 2026
# Problem 5: Draw squares using the turtle module

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

drawSquare(alex, 20)

alex.penup()
alex.backward(10)
alex.right(90)
alex.forward(10)
alex.left(90)
alex.pendown()
drawSquare(alex, 40)

alex.penup()
alex.backward(10)
alex.right(90)
alex.forward(10)
alex.left(90)
alex.pendown()
drawSquare(alex, 60)

alex.penup()
alex.backward(10)
alex.right(90)
alex.forward(10)
alex.left(90)
alex.pendown()
drawSquare(alex, 80)

wn.exitonclick()
