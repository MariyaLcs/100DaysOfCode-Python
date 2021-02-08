# https://docs.python.org/3/library/turtle.html
# https://cs111.wellesley.edu/labs/lab01/colors

from turtle import Turtle, Screen, forward, up, down

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
import random
#
# for i in range(3, 11):
#     timmy_the_turtle.color(random.random(), random.random(), random.random())
#     for _ in range(i):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360/i)

#Generate a random walk

for _ in range(100):
    timmy_the_turtle.speed(6)
    timmy_the_turtle.color(random.random(), random.random(), random.random())
    length = random.randint(0, 5) * 10
    random_generate = random.randint(1, 4)
    if random_generate == 1:
        timmy_the_turtle.forward(length)
    elif random_generate == 2:
        timmy_the_turtle.right(90)
        timmy_the_turtle.forward(length)
    elif random_generate == 3:
        timmy_the_turtle.right(-90)
        timmy_the_turtle.forward(length)
    else:
        timmy_the_turtle.backward(length)


screen = Screen()
screen.exitonclick()
