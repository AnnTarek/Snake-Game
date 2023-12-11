from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if food.distance(snake.snakes[0]) < 15:
        food.refresh()
        score.refresh_score()
        snake.update()
        snake.move()
    if snake.hit_a_wall() or snake.hit_tail():
        score.score_reset()
        snake.snake_reset()


screen.exitonclick()
