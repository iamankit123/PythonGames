# CANNON Ball program
from random import *
from turtle import *
from base import vector

balls = []
speeds = []
targets = []

def isInside(item):
    return -200 < item.x < 200 and -200 < item.y < 200

def draw_dot(v, size = 10, color = "black"):
    goto(v.x, v.y)
    dot(size, color)

def draw():
    #"Move ball and draw game."
    clear()
    for ball in balls:
        if isInside(ball):
            draw_dot(ball, 10, "red")
    for target in targets:
        if isInside(target):
            draw_dot(target, 20, "blue")
    update()

def tap(x,y):
    ball = vector(-199, -199)
    speed = vector((x+200)/25, (y+200)/25)
    balls.append(ball)
    speeds.append(speed)

def move():
    if randrange(50) == 0:
        y = randrange(-150,150)
        target = vector(200, y)   # Originate target on rightmost wall, at any random y coordinate
        targets.append(target)

    for target in targets:
        target.x -= 0.5
    new_balls = balls.copy()
    new_speeds = speeds.copy()
    balls.clear()
    speeds.clear()
    for ball, speed in zip(new_balls, new_speeds):
        if isInside(ball):
            speed.y -= 0.5
            ball.move(speed)
            balls.append(ball.copy())
            speeds.append(speed.copy())
    draw()

    # Now, to delete those targets that touch ball
    dup = targets.copy()
    targets.clear()
    for target in dup:
        for ball in balls:
            if abs(target - ball) > 13:
                targets.append(target)
    draw()

    # To finish game if any target touches left-most wall
    for target in targets:
        if not isInside(target):
            return
    ontimer(move, 50)



setup(420, 420, 370, 0)
hideturtle()
tracer(False)
onscreenclick(tap) # On mouse click, call function onscreenclick
up()
move()
draw()
done()

