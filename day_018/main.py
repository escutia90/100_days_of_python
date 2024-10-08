from turtle import Turtle, Screen
import random

screen = Screen()
turt = Turtle()
turt.shape("turtle")
turt.color("blue")
turt.speed("fastest")
# make asquare
# for i in range(4):
#     turt.forward(100)
#     turt.left(90)

#draw a dotted line

# for i in range(5):
#     turt.pendown()
#     turt.forward(20)
#     turt.penup()
#     turt.forward(20)

def draw_shape(obj, size_len, sides):
    angle = 360 / sides
    for i in range(sides):
        obj.forward(size_len)
        obj.right(angle)

#create shapes
# for i in range(3,10):
#     draw_shape(turt, 50, i)

#random walk
def random_walk(obj):
    while True:
        obj.forward(10)
        obj.setheading(random.randint(0,360))

# random_walk(turt)
for i in range(0,360,20):
    turt.setheading(turt.heading() + i) 
    turt.circle(60)

screen.exitonclick()