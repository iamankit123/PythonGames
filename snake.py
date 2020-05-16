from base import square, isInside, vector
from random import randrange
from turtle import *


snakes = [vector(randrange(-200, 200), randrange(-200, 200))]
food = vector(randrange(-200, 200), randrange(-200, 200))
direction = vector(-10,0)

def draw():
	clear()
	# Draw snake
	for snake in snakes:
		square(snake.x, snake.y, 9, "black")

	# Draw food
	square(food.x, food.y, 9, "red")

def change(x,y):
	direction.x = x
	direction.y = y
	

def move():
	global food
	#global snakes
	# Extend snake length
	head = snakes[0].copy()
	head.move(direction)
	if head in snakes or not isInside(head):
		square(head.x, head.y, 9, "red")
		update()
		return
	snakes.insert(0, head)
	if abs(food - head) < 8:
		food = vector(randrange(-200, 200), randrange(-200, 200))
	else:
		snakes.pop()

	draw()
	ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
up()
listen()
onkey(lambda:change(0,10), "Up")
onkey(lambda:change(0,-10), "Down")
onkey(lambda:change(-10,0), "Left")
onkey(lambda:change(10,0), "Right")
move()
done()
# On keyboard click
	
