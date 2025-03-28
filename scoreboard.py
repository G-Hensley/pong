"""
Scoreboard Module
---------------
Defines the Scoreboard class used to display and track scores in the Pong game.
Also handles displaying the game over message when a player wins.
"""
from turtle import Turtle
FONT = ("Arial", 30, 'bold')


class Scoreboard(Turtle):
    """
    Scoreboard class for the Pong game.
    Inherits from Turtle class and displays the current score and game over messages.
    """

    def __init__(self):
        """Initialize a new scoreboard with starting scores of 0."""
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("chartreuse")
        self.speed('fastest')
        self.left_score = 0
        self.right_score = 0

    def print_scores(self):
        """Display current scores at the top of the screen."""
        self.clear()
        self.goto(x=-100, y=245)
        self.write(arg=self.left_score, font=FONT)
        self.goto(x=85, y=245)
        self.write(arg=self.right_score, font=FONT)

    def game_over(self, loser_side, winner_side):
        """
        Display game over messages when a player reaches 5 points.
        
        Args:
            loser_side (tuple): Coordinates to display loser message
            winner_side (tuple): Coordinates to display winner message
        """
        self.color("chartreuse")
        self.goto(loser_side)
        self.write(arg="Game Over", font=FONT)
        self.goto(winner_side)
        self.write(arg="Winner!", font=FONT)
