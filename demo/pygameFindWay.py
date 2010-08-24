#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random, sys

from golem.grid import Grid
from golem.objects import BaseObject, MoveableObject
from golem.viewers import Pygame as Viewer

grid = Grid([10,10])
viewer = Viewer(grid, bg=(29,45,39), cellSize=[64,64])


# the only once moveable object - golem
golem = MoveableObject(grid=grid, image='images/golem.png')

# drawing background - grass
for i in range(10):
	for j in range(10):
		BaseObject(grid=grid, image='images/grass.png', position=(i, j), weight=0)

BaseObject(grid=grid, image='images/grass.png', position=(0, 0), weight=0)


# creating X walls
for i in range(40):
	grid.Collisions.append(
		grid.Collision(
			golem,
			BaseObject(grid=grid, image='images/wall.png', position=grid.randomPosition(), weight=20),

			canGoThrough=False
		)
	)


# creating X swamps
for i in range(40):
	grid.Collisions.append(
		grid.Collision(
			golem,
			BaseObject(grid=grid, image='images/swamp.jpg', position=grid.randomPosition(), weight=10),

			canGoThrough=True,
			speed=20
		)
	)

# setting good position of golem
while True:
	p = grid.randomObjectPosition(golem)

	if golem.setPosition(p):
		break



def exit():
	grid.tTimer.cancel()
	sys.exit()

viewer.events[viewer.pygame.QUIT] = exit


def click():
	x, y = viewer.getMousePosition()
	return golem.setPosition(x, y)

viewer.events[viewer.pygame.MOUSEBUTTONUP] = click



viewer.start()
