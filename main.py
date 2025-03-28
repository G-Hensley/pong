#!/usr/bin/env python3
"""
Pong Game
---------
A classic arcade Pong game implementation using Python's Turtle graphics.
The game features two paddles controlled by players and a ball that bounces
between them. First player to reach 5 points wins.

Controls:
- Right paddle: Up/Down arrow keys
- Left paddle: W/S keys
"""
from turtle import Screen, Turtle
from paddles import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

# Setup the main game window
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Draw the center dashed line
line_turtle = Turtle()
line_turtle.penup()
line_turtle.color("white")
line_turtle.speed("fastest")
line_turtle.goto(x=0, y=-280)
line_turtle.setheading(90)

for num in range(30):
    line_turtle.pendown()
    line_turtle.forward(10)
    line_turtle.penup()
    line_turtle.forward(10)

# Create game objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
game_ball = Ball()
score_board = Scoreboard()
score_board.print_scores()

# Setup keyboard controls
screen.listen()
screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key='s')

# Main game loop
game_on = True
while game_on:
    time.sleep(game_ball.ball_speed)
    screen.update()
    game_ball.move()

    # Detect collision with top and bottom walls
    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        game_ball.bounce_y()

    # Detect collision with paddles
    if game_ball.distance(r_paddle) < 45 and game_ball.xcor() > 320 or \
            game_ball.distance(l_paddle) < 45 and game_ball.xcor() < -320:
        game_ball.bounce_x()
        game_ball.move()

    # Detect when right paddle misses
    if game_ball.xcor() > 380:
        score_board.left_score += 1
        score_board.print_scores()
        game_ball.reset_ball()
    # Detect when left paddle misses
    elif game_ball.xcor() < -380:
        score_board.right_score += 1
        score_board.print_scores()
        game_ball.reset_ball()

    # Check for game over (first to 5 points)
    if score_board.left_score == 5:
        # Left player wins - display game over message
        # Format: (loser_side, winner_side)
        score_board.game_over((150, 100), (-150, 100))
        game_on = False
    elif score_board.right_score == 5:
        # Right player wins - display game over message
        # Format: (loser_side, winner_side)
        score_board.game_over((-150, 100), (150, 100))
        game_on = False

# Exit the game when clicked
screen.exitonclick()
