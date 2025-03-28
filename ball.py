"""
Ball Module
----------
Defines the Ball class used in the Pong game.
The ball moves around the screen, bounces off walls and paddles,
and increases in speed after each paddle hit.
"""
from turtle import Turtle


class Ball(Turtle):
    """
    Ball class for the Pong game.
    Inherits from Turtle class and represents the ball that moves between paddles.
    """

    def __init__(self):
        """Initialize a new ball at the center of the screen."""
        super().__init__()
        self.shape('circle')
        self.color("white")
        self.penup()
        self.y_move = 3
        self.x_move = 3
        self.ball_speed = 0.02

    def move(self):
        """Move the ball based on current x and y movement values."""
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        """Reverse the vertical direction when hitting top or bottom walls."""
        self.y_move *= -1

    def bounce_x(self):
        """
        Reverse the horizontal direction when hitting a paddle.
        Also increases the ball speed to make the game progressively harder.
        """
        self.x_move *= -1
        # Multiply by 0.9 to reduce the delay (making ball faster)
        # Lower ball_speed value = faster ball movement
        self.ball_speed *= 0.9

    def reset_ball(self):
        """
        Reset the ball position and speed after a point is scored.
        Ball returns to center and moves in the opposite direction.
        """
        self.goto(0, 0)
        self.ball_speed = 0.02
        self.x_move *= -1
        self.y_move = 2
