#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import re
from os import path

import apps.BaseApp
import ConfigParser

import grid.Grid


patternFunction = re.compile("[a-zA-Z]*")

class AppFromConfigFile(apps.BaseApp):
	title = ''

	_config = None
	_objects = {}

	collisions = {}

	def __init__(self):
		self.init()

		# The order in which are calling function.
		# The order is very important.
		self.configStructure = {
			1 : ['app', self.setApp],
			2 : ['grid', self.setGrid],
			3 : ['viewer', self.setViewer], # need grid
			4 : ['object', self.setObject], # need grid
			5 : ['collision', self.setCollision], # need grid, objects
			6 : ['control', self.setControl], # need viewer, objects
		}

		self.beforeConfig()
		self.setCollisions()
		self.loadConfig(self.config)
		self.afterConfig()

	def beforeConfig(self):
		pass

	def loadConfig(self, configFile):
		"""
		Function from loading config from config file,
		parsing it and then to call functions to work up it
		"""

		self._config = ConfigParser.ConfigParser()
		self._config.read(configFile)

		# split sections by pattern:
		# [section.option]
		sectionNames = []
		sectionsInDict = []
		for original in self._config.sections():
			option = ''
			if '.' in original:
				section, option = original.split('.')
			else:
				section = original

			sectionNames.append(section)
			sectionsInDict.append({'original':original, 'name':section, 'option':option})

		# list for sorted sections
		sections = []

		# dict to saving a function to call with some section
		calledFunctions = {}

		# sorting sections by structure, set in self.configStructure
		for i in self.configStructure:
			# getting section name from structure
			sectionName = self.configStructure[i][0]

			while sectionName in sectionNames:
				# append to sorted sectios
				sections.append(sectionsInDict[sectionNames.index(sectionName)])

				del sectionsInDict[sectionNames.index(sectionName)]
				sectionNames.remove(sectionName)

			calledFunctions[sectionName] = self.configStructure[i][1]

		# walk in sections and calling function to work on
		for section in sections:
			if not calledFunctions.has_key(section['name']):
				continue

			# calling function from structure
			calledFunctions[section['name']](
				section = section['name'],
				config  = self._config,
				option  = section['option'],
				items   = self._itemsToDict(self._config.items(section['original'])),
				options = self._config.options(section['original']),
			)

	def _itemsToDict(self, items):
		"""
		Function to convert items from list (x, y) to
		dict[x] = y.
		"""
		dict = {}
		for item in items:
			dict[item[0]] = item[1]

		return dict

	def afterConfig(self):
		pass

	def setApp(self, **params):
		"""
		Setting of the application from config file.
		"""

		for item in params['items']:
			self.__dict__[item] = params['items'][item]

	def setGrid(self, **params):
		"""
		Function to create and set grid from config file.
		"""
		self.grid = grid.Grid()
		items = params['items']

		if items.has_key('width') and items.has_key('height'):
			self.grid.setSize([int(items['width']), int(items['height'])])

	def setViewer(self, **params):
		"""
		Function to create and set viewer from config file
		"""

		items = params['items']
		viewerName = items.pop('viewer')

		try:
			exec('import viewers.'+viewerName+' as Viewer')
		except:
			raise Exception('Can\'t load viewer '+viewerName, sys.exc_info())

		# create viewer
		self.viewer = Viewer(grid=self.grid)
		self.viewer.title = self.title

		# convert strings in list to integers
		self.viewer.bg = [int(i) for i in items['bg'].split(',')]

		if items.has_key('cellsize'):
			# set size by size of cell
			self.viewer.setSizeByCell(int(items.pop('cellsize')))

		if items.has_key('drawgrid'):
			if items['drawgrid'].lower()=="true":
				self.viewer.drawGrid = True

	def setObject(self, **params):
		"""
		Function to create new object from config file,
		locate it and add to the grid.
		"""

		objectType = params['items'].pop('type')

		try:
			exec('import objects.'+objectType+' as Object')
		except:
			raise Exception('Can\'t load object type '+objectType, sys.exc_info())

		# creating object
		object = Object(grid=self.grid)
		object.name = params['option']

		# setting image
		if params['items'].has_key('image'):
			object.setImage(path.join(self.images_dir, params['items'].pop('image')))

		# setting position
		if params['items'].has_key('position'):
			pos = params['items'].pop('position')

			if pos=="random":
				# generate random position
				pos = self.grid.randomPosition()
			else:
				x, y = pos.split(',')

				if x.lower()=="max":
					x = self.grid.getSize()[0]-1
				if y.lower()=="max":
					y = self.grid.getSize()[1]-1

				# position from config file
				pos = (int(x), int(y))

			# relocate object in grid
			if self.grid.teleport(object, pos):
				object.position = pos

		# to possibility to control the object
		if params['items'].has_key('control'):
			self.setControl(object=object, control=params['items'].pop('control'))

		# setting weight of the object - important for rendering
		if params['items'].has_key('weight'):
			object.weight = int(params['items'].pop('weight'))

		# setting all others options in config file
		object.set(params['items'])

		# saving object to dict
		self._objects[object.name] = object

	def setCollision(self, **params):
		"""
		Function for setting collisions from config file
		"""

		# getting objects names
		primaryName, secondaryName = params['option'].split(':')

		# getting objects instances
		primaryObject = self._objects[primaryName]
		secondaryObject = self._objects[secondaryName]

		# default values of collision
		result = True
		speed = 100
		onCollision = None

		# setting the result of the collision
		if params['items'].has_key('result'):
			if params['items']['result'].lower()=="false":
				result = False

		# setting the speed of collision
		if params['items'].has_key('speed'):
			speed = int(params['items']['speed'])

		# setting function called after collision
		if params['items'].has_key('oncollision'):
			name = params['items'].pop('oncollision')
			if self.collisions.has_key(name):
				onCollision = self.collisions[name]

		# adding collision to register
		self.grid.Collisions.append(
			self.grid.Collision(
				primaryObject,
				secondaryObject,

				result = result,
				speed  = speed,
				onCollision = onCollision
			)
		)

	def setControl(self, **params):
		"""
		Function to set control of the application or
		of the object.
		"""

		if not params.has_key('items'):
			params['items'] = params

		controlName = params['items']['control']

		try:
			exec('import controls.'+controlName+' as Control')
		except:
			raise Exception('Can\'t load control '+controlName, sys.exc_info())

		# creating new control
		control = Control(self)

		# if it is a control of object → setting object
		if params['items'].has_key('object'):
			control.setObject(params['items']['object'])

		# merge new controls with old controls in self.viewer.events
		self.viewer.events.update(control.getList())

		# saving of backtracking
		for event in control.getList():
			self.viewer.eventsControls[event] = control

