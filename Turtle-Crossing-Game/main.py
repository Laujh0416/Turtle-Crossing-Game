from turtle import Screen
from car import Car
from scoreboard import Scoreboard
from player import Player
import time


screen = Screen()
screen.colormode(255)

scoreboard = Scoreboard()

player = Player()
game_is_on = True

screen.bgcolor('#e9edc9')
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0.1)


car =Car()

def move():
    player.forward(10)

screen.listen()
screen.onkeypress(move, "Up")

num = 0.1

while game_is_on:
    screen.update()
    time.sleep(num)
    if player.ycor() == 280:
        scoreboard.score_num()
        player.refresh()
        num *= 0.9
    for i in car.car_segment_list:
        if player.distance(i) < 25:
            scoreboard.game_over()
            scoreboard.end_level_show()
            screen.bgcolor('black')
            game_is_on = False

    car.move_forward()







screen.exitonclick()
