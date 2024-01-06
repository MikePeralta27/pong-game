from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.goto(0, 0)
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self) -> None:
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(x=new_x, y=new_y)
        # self.setheading(40)
        # self.forward(1)