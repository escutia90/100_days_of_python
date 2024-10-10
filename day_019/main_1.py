from turtle import Turtle, Screen

turt = Turtle()
turt2 = Turtle()
screen = Screen()
screen.listen()

turt2.color("red")
turt2.teleport(0,20)

def move_forward():
    turt.forward(3)

def move_backwards():
    turt.backward(3)

def move_right():
    turt.right(10)

def move_left():
    turt.left(10)

def clear_screen():
    turt.home()
    turt.clear()

screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear_screen, "c")

screen.exitonclick()