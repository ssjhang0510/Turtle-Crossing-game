import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=turtle.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    # Detect collision with car
    for i in car_manager.all_cars:
        if turtle.distance(i) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect successful crossing
    if turtle.ycor() > 280:
        turtle.goto(0, -280)
        scoreboard.level_up()
        car_manager.speed_up()

screen.exitonclick()
