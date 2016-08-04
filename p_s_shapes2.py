from turtle import *
def draw(number_sides):
    for i in range(number_sides):
        forward(50)
        right(360/number_sides)
    penup()
    left(180-(360/number_sides))
    pendown()

for j in range(100):
    draw(3)
