# Kaiden Rivera
# 10/21/26
# P4LAB1
# This program uses turtle to draw a house (square and triangle).

# Importing Library
import turtle

# Create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()


# Set turtle options
pen.pensize(5)
pen.pencolor("Red")
pen.fillcolor("Red")
pen.shape("arrow")

# Code to draw shapes
for side in range(5):
    pen.forward(100)
    pen.left(90)
pen.forward(100)
pen.right(90)

# While loop that executes 3 times
sides = 3
pen.begin_fill()
while sides > 0:
    pen.left(120)
    pen.forward(100)
    sides = sides - 1
pen.end_fill()

pen.right(90)
pen.forward(50)
pen.left(90)

for side in range(4): # Mansion side-blocks (right side)
    pen.forward(50)
    pen.right(90)

pen.right(90) # Code to move to the opposite side
pen.forward(50)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(50)
pen.left(90)

for side in range(4): # Mansion side-blocks (left side)
    pen.forward(50)
    pen.left(90)

# Wait for user to close window
win.mainloop()
