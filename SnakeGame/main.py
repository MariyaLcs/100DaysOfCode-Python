from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
starting_positions = [(0, 0), (-20, 0), (-40, 0)]


for s_index in starting_positions:
    s = Turtle(shape="turtle")
    s.color("white")
    s.penup()
    s.goto(s_index)


screen.exitonclick()
