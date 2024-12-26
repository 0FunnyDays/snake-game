from turtle import Screen
from food import Food
from snake import Snake
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600) # you can choose what ever screen size you like just make sure you change the ->
#Collision coordinates by half the size you choose in each x and y -10 (-10 because it works the best).

screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
#Choose what ever keys you like.
screen.onkey(snake.up, "w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")


game_is_on = True
game_speed = 0.1

# Start the game loop
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

      # Increase speed by reducing delay
        if game_speed > 0.02:
            game_speed -= 0.1

    #Detect collision with wall
    if snake.head.xcor() >290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()


    #Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    #If head collides with any segment in the tail:
        #trigger game_over


screen.exitonclick()
