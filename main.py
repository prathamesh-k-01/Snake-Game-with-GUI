from turtle import Screen
import player
import time
from sanke import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.update()


def details():
    player

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision of food and snake
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if int(snake.head.xcor()) >= 300 or int(snake.head.xcor()) <= -300 or int(snake.head.ycor()) <= -300 or \
            int(snake.head.ycor()) >= 264:
        scoreboard.reset()
        # scoreboard.clear()
        food.clear()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()