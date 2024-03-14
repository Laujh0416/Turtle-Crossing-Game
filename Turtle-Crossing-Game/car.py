from turtle import Turtle
import random
import time

CAR_COLOURS = [
    (34, 34, 59),
    (74, 78, 105),
    (154, 140, 152),
    (201, 173, 167),
    (242, 233, 228)
]

class Car():
    def __init__(self):
        self.car_segment_list = []
        self.car_segment()



    def car_segment(self):
        car = Turtle()
        car.penup()
        new_x = 320
        new_y = random.randint(-250, 280)
        car.goto(new_x, new_y) 
        car.left(180)
        car.shape("square")
        car.turtlesize(stretch_len=2, stretch_wid=1)
        car.color(random.choice(CAR_COLOURS))
        self.car_segment_list.append(car)
    
    def move_forward(self):
        for i in self.car_segment_list:
            i.forward(10)
            if i.xcor() == 160:
                self.car_segment()


    
