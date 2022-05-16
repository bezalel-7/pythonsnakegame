from turtle import Screen

H = 0
f = open("score.txt", mode="w")
f.write(str(H))
f.close()
from snake import Snake
from food import Food
import time
from scoreboard import Scorecard

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
score = 0
snake = Snake()
food = Food()
scorboard = Scorecard()
game_is_on = True
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scorboard.increase_score()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scorboard.reset()
            snake.reset()

    if (snake.head.xcor() > 280 or snake.head.xcor() < -300) or (snake.head.ycor() > 300 or snake.head.ycor() < -300):
        scorboard.reset()
        snake.reset()

# pen = turtle.Turtle()
# pen.color("White")
# pen.write("GAME OVER!!",align="center", font=("Calibri",20, "bold"))

screen.exitonclick()
