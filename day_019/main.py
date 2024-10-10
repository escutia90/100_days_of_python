from turtle import Turtle, Screen
import random

colors = ["blue","green","red","orange","pink","purple"]
turtles = []
guess = int(input("Make a guess, which turtle is going to win?: "))

#create turtles
for i in range(6):
    turtles.append(Turtle("turtle"))
    turtles[i].color(colors[i])

#setup screen parameters
screen = Screen()
screen_height = screen.window_height()
screen_width = screen.window_width()
END_OF_RACE = screen_width/2 + abs(turtles[0].xcor())
has_race_ended = False

#position the turtles
start_y_pos = 200
for i in turtles:
    i.teleport(-200,start_y_pos)
    start_y_pos -= 60

#advance all turtles
while has_race_ended != True:

    for index, t in enumerate(turtles):
        distance = random.randint(1, 10)
        t.forward(distance)
        if t.xcor() >= END_OF_RACE:
            print(f"turtle {index} won")
            has_race_ended = True
            if guess == index:
                print("your turtle won!")
            else:
                print("you guessed incorrectly")


screen.listen()
screen.exitonclick()