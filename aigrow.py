import turtle
import random

# Set up the turtle screen
turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()


# Function to draw a petal
def draw_petal():
    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(50, 60)
    turtle.left(120)
    turtle.circle(50, 60)
    turtle.end_fill()


# Function to draw a rose
def draw_rose():
    turtle.penup()
    turtle.goto(random.randint(-200, 200), random.randint(-200, 200))
    turtle.pendown()

    # Draw petals
    for _ in range(6):
        draw_petal()
        turtle.left(60)

    # Draw the center of the rose
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()


# Function to draw a stem
def draw_stem():
    turtle.color("green")
    turtle.width(5)
    turtle.forward(100)
    turtle.backward(150)


# Draw multiple roses with stems
for _ in range(5):
    draw_rose()
    draw_stem()

# Close the turtle graphics window on click
turtle.exitonclick()
