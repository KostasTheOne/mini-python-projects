from turtle import Screen
import time
from snake import Snake
from scoreboard import Score
from food import Food

segments=[]
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)
snake=Snake()
food=Food()
score=Score()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

score.update_score()

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        score.reset()
        snake.reset()

    if snake.head.distance(food)<15:
        screen.update()
        food.refresh()
        snake.extend()
        score.add_score()
    for segment in snake.segments[1:]:
            if snake.head.distance(segment)<10:
                score.reset()
                snake.reset()

screen.exitonclick()