#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random, sys

from golem.grid import Grid
from golem.objects import BaseObject, MoveableObject
from golem.viewers import Pygame as Viewer

grid = Grid([10,10])
viewer = Viewer(grid, bg=(29,45,39), cellSize=[64,64])

# drawing background - grass
for i in range(10):
	for j in range(10):
		a = BaseObject(grid=grid, image='images/grass.png', position=(i, j))

# the only once moveable object - golem
golem = MoveableObject(grid=grid, image='images/golem.png')

# creating X walls
for i in range(30):
	grid.Collisions.append(
		grid.Collision(
			golem,
			BaseObject(grid=grid, image='images/wall.png', position=grid.randomPosition()
		),
		canGoThrough=False)
	)

# setting good position of golem
while not golem.setRandomPosition():
	pass

def exit():
	grid.tTimer.cancel()
	sys.exit()

viewer.events[viewer.pygame.QUIT] = exit

def nahoru():
	x, y = golem.getPosition()
	golem.setPosition(x, y-1)
viewer.events[viewer.pygame.K_UP] = nahoru

def dolu():
	x, y = golem.getPosition()
	golem.setPosition(x, y+1)
viewer.events[viewer.pygame.K_DOWN] = dolu

def doleva():
	x, y = golem.getPosition()
	golem.setPosition(x-1, y)
viewer.events[viewer.pygame.K_LEFT] = doleva

def doprava():
	x, y = golem.getPosition()
	golem.setPosition(x+1, y)
viewer.events[viewer.pygame.K_RIGHT] = doprava

viewer.start()
