"""
Paddle Module
------------
Defines the Paddle class used for player-controlled paddles in the Pong game.
Each paddle can move up and down vertically along the screen edges.
"""
from turtle import Turtle


class Paddle(Turtle):
    """
    Paddle class for the Pong game.
    Inherits from Turtle class and represents a player-controlled paddle.
    """

    def __init__(self, coordinates):
        """
        Initialize a new paddle at the specified coordinates.
        
        Args:
            coordinates (tuple): The x, y position to place the paddle
        """
        super().__init__()
        self.color("white")
        self.shape('square')
        self.setheading(90)
        self.shapesize(1, 4)
        self.coordinates = coordinates
        self.penup()
        self.goto(coordinates)

    def move_up(self):
        """Move the paddle upward on the screen, stopping at the upper boundary."""
        new_y = self.ycor() + 10
        # Check if paddle would go off the top of the screen
        if new_y < 250:
            self.goto(x=self.xcor(), y=new_y)

    def move_down(self):
        """Move the paddle downward on the screen, stopping at the lower boundary."""
        new_y = self.ycor() - 10
        # Check if paddle would go off the bottom of the screen
        if new_y > -250:
            self.goto(x=self.xcor(), y=new_y)
