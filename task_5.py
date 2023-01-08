from turtle import *

speed("fastest")

starting_pos = pos()

for i in range(360):
    forward(5 * (i % 60))
    right(1)
    setposition(starting_pos)
setheading(360//12)
for i in range(360):
    forward(5 * (i % 60))
    right(1)
    setposition(starting_pos)

exitonclick()
