from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard, Boundaryline
import time

# Set up the game screen
screen = Screen()
screen.setup(width=600, height=600)  # Set screen dimensions
screen.bgcolor("black")              # Set background color
screen.title("My Snake Game")        # Set window title
screen.tracer(0)                     # Disable automatic screen updates


snake = Snake()        
food = Food()           
scoreboard = ScoreBoard() 
boundaryline = Boundaryline() 

# Set up keyboard controls
screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')


game_is_on = True
while game_is_on:
    screen.update()     # Update the screen manually
    time.sleep(0.2)     # Control game speed
    snake.move()        # Move the snake continuously

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()          # Move food to new location
        snake.extend()           # Add new segment to snake
        scoreboard.increase_score()  # Update score

    # Detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 245 or snake.head.ycor() < -280:
        game_is_on = False       # End game
        scoreboard.game_over()   # Display game over message

    # Detect collision with tail
    for segment in snake.segments[1:]:  # Skip head segment check
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# Exit the game when clicked
screen.exitonclick()
