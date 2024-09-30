from turtle import Turtle, Screen

tortuga = Turtle()
tortuga.shape("turtle")
tortuga.color("DarkSeaGreen4")

myScreen = Screen()
print(myScreen.canvheight)

tortuga.forward(100)

myScreen.exitonclick()