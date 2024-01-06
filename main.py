from turtle import Screen, Turtle
from paddle import Paddle

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-380, 0))


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(n=0)


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()