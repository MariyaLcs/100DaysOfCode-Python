from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for s_index in starting_positions:
    s = Turtle(shape="turtle")
    s.color("white")
    s.penup()
    s.goto(s_index)
    segments.append(s)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

screen.exitonclick()
