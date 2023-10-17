import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Setup turtle and moves it
turtle = Player()
screen.listen()
screen.onkey(turtle.move, "w")

scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Checks if turtle gets to finish line
    if turtle.ycor() > 280:
        turtle.goto(STARTING_POSITION)
        scoreboard.level_up()
        scoreboard.update_scoreboard()
        car_manager.increment_speed()

    # Detects collision between turtle and car
    for car in car_manager.cars:
        if car_manager.is_collision(turtle, car):
            scoreboard.game_over()
            game_is_on = False

screen.mainloop()

