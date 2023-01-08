from turtle import *
from random import randint

speed("slow")

step = 10
mount = [0, 30, 50, 80, 100, 150, 155, 170, 190, 230, 210, 195, 170, 160, 145, 120, 100, 95, 70, 35, 15, 0]
forward(2 * len(mount) * step + step)
for i in range(len(mount)):
    if mount[i] <= 20:
        goto(step + i * step, mount[i])
    else:
        goto(step + i * step, mount[i] + randint(-20, 20))
forward(step)
for i in range(len(mount)):
    if mount[i] <= 20:
        goto(step + (len(mount) + i) * step, mount[i])
    else:
        goto(step + (len(mount) + i) * step, mount[i] + randint(-20, 20))

exitonclick()
