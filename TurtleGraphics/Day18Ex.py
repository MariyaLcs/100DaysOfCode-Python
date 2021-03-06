# https://docs.python.org/3/library/turtle.html
# https://cs111.wellesley.edu/labs/lab01/colors

from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("DarkOrchid")

# Draw a line
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# Draw a Dashed line
# for _ in range(20):
#     timmy_the_turtle.forward(5)
#     timmy_the_turtle.up()
#     timmy_the_turtle.forward(5)
#     timmy_the_turtle.down()

# Drawing Different Shapes
# import random
#
# for i in range(3, 11):
#     timmy_the_turtle.color(random.random(), random.random(), random.random())
#     for _ in range(i):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360/i)

# Generate a random walk
# import random

# directions = [0, 90, 180, 270]
# for _ in range(100):
#     timmy_the_turtle.speed(6)
#     timmy_the_turtle.pensize(12)
#     timmy_the_turtle.color(random.random(), random.random(), random.random())
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(directions))

# Draw a Spirograph
import random

timmy_the_turtle.speed(15)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy_the_turtle.color(random.random(), random.random(), random.random())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)


draw_spirograph(5)


screen = Screen()
screen.exitonclick()
