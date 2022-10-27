import turtle as trt
import random

# settings
trt.setup(800, 800, 0, 0)
trt.pensize(2)
tt_pencolor = ['red', 'orange', 'yellow', 'purple', 'blue']
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
        trt.pencolor(random.choice(tt_pencolor))
        trt.pendown()
        trt.fd(distance)
        trt.left(angle)
        a += 180 - angle
        # print(a)

    trt.done()

turtle_movement2(170, 600)