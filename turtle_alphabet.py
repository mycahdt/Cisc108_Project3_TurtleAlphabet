# Project 3- Turtle Alphabet
# If you got help from anyone, please write their emails here:
#  1) acbart@udel.edu
#  2) ...

###############################################################
# Part 1) Setup
# Load turtle module, move it to left side, make turtle faster
import turtle
turtle.reset()
turtle.speed(10)
turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
turtle.speed(3)

###############################################################
# Part 2) Drawing
# Write the code for each letter below

# First letter
# ...
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(50)
turtle.backward(50)
turtle.left(90)
turtle.forward(30)

# Leave space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# Second letter
# ...

###############################################################
# Part 3) Wrap-up
# Start the turtles!
turtle.mainloop()
