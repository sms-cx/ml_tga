import turtle as trt
import random

# settings
trt.setup(800, 800, 0, 0)
trt.pensize(2)
tt1_pencolor = ['#FFBE86', '#FFE156', '#FFE9CE', '#FFB5C2', '#BD4F6C']
tt2_pencolor = ['#ffbe0b', '#fb5607', '#ff006e', '#8338ec', '#3a86ff']
tt3_pencolor = ['#9CFFFA', '#e6af2e', '#3d348b', '#885a5a', '#f6511d']
trt.speed(200)
trt.ht()
x = 0

# turtle movement
def turtle_movement2(angle, distance):
    trt.bk(distance/2)
    a = 0
    while True:
        if a >= 360:
            break
        trt.pencolor(random.choice(tt3_pencolor))
        trt.pendown()
        trt.fd(distance)
        trt.left(angle)
        a += 180 - angle
        # print(a)

    trt.done()

turtle_movement2(145, 600)