import turtle

screen = turtle.Screen()
screen.setup(width = 600, hight = 600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = turtle.Turtle()
snake.shape("square")
snake.color("white")
snake.goto(0, 0)
snake.penup