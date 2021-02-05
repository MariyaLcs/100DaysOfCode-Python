#https://docs.python.org/3/library/turtle.html
#https://cs111.wellesley.edu/labs/lab01/colors

from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("DarkOrchid")

# Draw a line
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# Draw a Dashed line
for _ in range(20):
    timmy_the_turtle.forward(5)
    timmy_the_turtle.up()
    timmy_the_turtle.forward(5)
    timmy_the_turtle.down()











screen = Screen()
screen.exitonclick()