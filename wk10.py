import turtle

def koch(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3
        koch(t, length, level - 1)
        t.left(60)
        koch(t, length, level - 1)
        t.right(120)
        koch(t, length, level - 1)
        t.left(60)
        koch(t, length, level - 1)

# Set up turtle
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed

# Move turtle to starting position
t.penup()
t.goto(-150, 90)
t.pendown()

# Draw Koch snowflake
for _ in range(3):
    koch(t, 300, 3)  # (turtle, side length, recursion level)
    t.right(120)

# Finish
turtle.done()
