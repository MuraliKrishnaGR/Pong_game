from turtle import Screen, Turtle
from paddle1 import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up the screen for the Pong game
screen = Screen()
screen.bgcolor("black")  # Set the background color to black
screen.setup(width=800, height=600)  # Set the screen dimensions
screen.title("Pong")  # Set the title of the game window
screen.tracer(0)  # Turn off automatic animation updates for smoother gameplay

# Create paddles, ball, and scoreboard
r_paddle = Paddle((350, 0))  # Right paddle at position (350, 0)
l_paddle = Paddle((-350, 0))  # Left paddle at position (-350, 0)
ball = Ball()  # Create a ball object
scoreboard = Scoreboard()  # Create a scoreboard to track scores

# Set up keyboard listeners for paddle movement
screen.listen()
screen.onkey(r_paddle.go_up, "Up")  # Right paddle moves up with the "Up" arrow key
screen.onkey(r_paddle.go_down, "Down")  # Right paddle moves down with the "Down" arrow key
screen.onkey(l_paddle.go_up, "w")  # Left paddle moves up with the "W" key
screen.onkey(l_paddle.go_down, "s")  # Left paddle moves down with the "S" key

# Game loop to keep the game running
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # Control the speed of the game (faster as the game progresses)
    screen.update()  # Update the screen to reflect changes
    ball.move()  # Move the ball based on its current direction

    # Detect collision with the top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()  # Reverse the ball's vertical direction (bounce off the wall)

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()  # Reverse the ball's horizontal direction (bounce off the paddle)

    # Detect when the right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()  # Reset the ball to the center of the screen
        scoreboard.l_point()  # Left player gets a point

    # Detect when the left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()  # Reset the ball to the center of the screen
        scoreboard.r_point()  # Right player gets a point

# Keep the game window open until clicked
screen.exitonclick()
