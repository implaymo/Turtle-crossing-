import random
import turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.car = []
        pass

    def create_car(self):
        new_car = turtle.Turtle("square")
        new_car.shapesize(2, 1)
        new_car.color(random.choice(COLORS))
        new_car.penup()


