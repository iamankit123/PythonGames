from turtle import *
from base import *
spin = 0

def draw_wing(angle, color):
	right(angle)
	forward(100)
	dot(120, color)
	back(100)

def draw():
	global spin
	clear()
	angle = spin/10

	draw_wing(angle, "red")
	draw_wing(120, "blue")
	draw_wing(120, "green")
	right(120)
	update()

def slow_spinner():
	global spin
	if spin > 0:
		spin -= 1
	draw()
	ontimer(slow_spinner, 50)

def onSpace():
	global spin
	spin += 10


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
listen()
onkey(onSpace, "space")
slow_spinner()
done()
		
