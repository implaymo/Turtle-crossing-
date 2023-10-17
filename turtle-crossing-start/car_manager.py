import random
import turtle
from random import randint


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []

    def create_car(self):
        random_chance = randint(0,6)
        if random_chance == 1:
            new_car = turtle.Turtle("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            y_position = randint(-250, 260)
            new_car.goto(300, y_position)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)


    def is_collision(self, turtle, car):
        distance = turtle.distance(car)
        return distance < 20

    def increment_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
