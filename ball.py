from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.goto(0, 0)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_sleep = 0.1

    def move(self) -> None:
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self) -> None:
        self.y_move *= -1

    def bounce_x(self) -> None:
        self.x_move *= -1
        self.move_sleep *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_sleep = 0.1
        self.bounce_x()
