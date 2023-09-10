from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_new_car(self):
        new_car = Turtle('square')
        new_car.penup()
        new_car.setheading(180)
        new_car.turtlesize(stretch_wid=1, stretch_len=2)
        new_car.color(choice(COLORS))
        new_car.goto(300, randint(-250, 250))
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def increment_speed(self):
        self.car_speed += MOVE_INCREMENT

