import turtle
import os

window = turtle.Screen()
window.title("Pong by @Jenna")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle 1
first_pad = turtle.Turtle()  # turtle object
first_pad.speed(0)           # speed of turtle module
first_pad.shape("square")
first_pad.color("light blue")
first_pad.shapesize(stretch_wid=5, stretch_len=1)
first_pad.penup()            # doesn't draw a line
first_pad.goto(-350, 0)      # x and y coord

# Paddle 2
sec_pad = turtle.Turtle()    # turtle object
sec_pad.speed(0)             # speed of turtle module
sec_pad.shape("square")
sec_pad.color("light blue")
sec_pad.shapesize(stretch_wid=5, stretch_len=1)
sec_pad.penup()              # doesn't draw a line
sec_pad.goto(350, 0)         # x and y coord

# Ball
ball = turtle.Turtle()       # turtle object
ball.speed(10)               # speed of turtle module
ball.shape("circle")
ball.color("red")
ball.penup()                 # doesn't draw a line
ball.goto(0, 0)              # x and y coord
ball.dx = 0.9                # increase speed of ball
ball.dy = -0.9               # increase speed of ball

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def paddle1_up():
    y = first_pad.ycor()     # y coord in turtle module
    y += 20                  # adds 20 pixels to y
    first_pad.sety(y)

def paddle1_down():
    y = first_pad.ycor()     # y coord in turtle module
    y -= 20                  # adds 20 pixels to y
    first_pad.sety(y)

def paddle2_up():
    y = sec_pad.ycor()       # y coord in turtle module
    y += 20                  # adds 20 pixels to y
    sec_pad.sety(y)

def paddle2_down():
    y = sec_pad.ycor()       # y coord in turtle module
    y -= 20                  # adds 20 pixels to y
    sec_pad.sety(y)

# Keyboard Binding
window.listen()                      # tells program to listen for keyboard input
window.onkeypress(paddle1_up, "w")   # calls function when user presses w (first paddle)
window.onkeypress(paddle1_down, "s")
window.onkeypress(paddle2_up, "Up")
window.onkeypress(paddle2_down, "Down")

# Main game loop
game_on = True

while game_on:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1       # reverses the direction of ball

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        if score_a == 7:
            pen.clear()
            pen.write("Player A Wins!", align="center", font=("Courier", 36, "normal"))
            game_on = False

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        if score_b == 7:
            pen.clear()
            pen.write("Player B Wins!", align="center", font=("Courier", 36, "normal"))
            game_on = False

    # Bounce off paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < sec_pad.ycor() + 40 and ball.ycor() > sec_pad.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < first_pad.ycor() + 40 and ball.ycor() > first_pad.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

# Keep the window open
while True:
    window.update()

