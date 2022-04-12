import turtle
import random
import time

lives = 3
score = 0

window = turtle.Screen()
window.tracer(0)
window.title("Pacman")
window.bgcolor("black")
window.setup(800, 600)

pacman = turtle.Turtle()
pacman.speed(0)
pacman.penup()
pacman.color("yellow")
pacman.shape("circle")
pacman.direction = "stop"

pen = turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.goto(0, 245)
pen.pendown()
pen.write("Score {} Lives {}".format(score, lives), align="center", font=("Courier", 36))
pen.hideturtle()

foods = []
for _ in range(40):
    food = turtle.Turtle()
    food.speed(0)
    food.penup()
    food.color("orange")
    food.shape("circle")
    food.shapesize(stretch_wid=0.4, stretch_len=0.4)
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    food.setposition(x, y)
    foods.append(food)

def movement():
    if pacman.direction == "up":
        y = pacman.ycor()
        y += 0.7
        pacman.sety(y)

    if pacman.direction == "down":
        y = pacman.ycor()
        y -= 0.7
        pacman.sety(y)

    if pacman.direction == "left":
        x = pacman.xcor()
        x -= 0.7
        pacman.setx(x)

    if pacman.direction == "right":
        x = pacman.xcor()
        x += 0.7
        pacman.setx(x)

def moveUp():
    pacman.direction = "up"

def moveDown():
    pacman.direction = "down"

def moveLeft():
    pacman.direction = "left"

def moveRight():
    pacman.direction = "right"

window.listen()
window.onkeypress(moveUp, "Up")
window.onkeypress(moveDown, "Down")
window.onkeypress(moveLeft, "Left")
window.onkeypress(moveRight, "Right")


while True:
    window.update()

    if pacman.xcor() > 400 or pacman.xcor() <- 400 or pacman.ycor() > 300 or pacman.ycor() <- 300:
        lives -= 1
        pen.clear()
        pen.write("Score {} Lives {}".format(score, lives), align="center", font=("Courier", 36))
        time.sleep(1)
        pacman.goto(0, 0)

    if lives == 0:
        score = 0
        lives = 3
        pen.clear()
        pen.write("Score {} Lives {}".format(score, lives), align="center", font=("Courier", 36))
        time.sleep(1)
        pacman.goto(0, 0)

    for food in foods:
        if pacman.distance(food) < 10:
            score += 1
            pen.clear()
            pen.write("Score {} Lives {}".format(score, lives), align="center", font=("Courier", 36))
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            food.goto(x, y)

    movement()