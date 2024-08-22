from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, postion):
        super().__init__()
        self.shape("square")  # Create a new turtle for each segment
        self.color("white")  # Set the segment color to white
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()  # Prevent drawing lines while moving the turtle
        self.goto(postion)  # Move the segment to its position
        self.go_up()
        self.go_down()

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



