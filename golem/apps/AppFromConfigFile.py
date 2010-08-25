#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
from os import path

import apps.BaseApp
import ConfigParser

import grid.Grid


class AppFromConfigFile(apps.BaseApp):
	_config = None
	_objects = {}

	def __init__(self):

		self.structure = {
			1 : ['app', self.setApp],
			2 : ['grid', self.setGrid],
			3 : ['viewer', self.setViewer],
			4 : ['object', self.setObject],
			5 : ['collision', self.setCollision],
			6 : ['control', self.setControl],
		}

		self.init()
		self.loadConfig(self.config)

	def init(self):
		pass

	def loadConfig(self, file):
		self._config = ConfigParser.ConfigParser()
		self._config.read(file)

		originalSections = self._config.sections()

		loadedSections = []
		for i, section in enumerate(originalSections):
			if '.' in section:
				section, option = section.split('.')
			loadedSections.append(section)

		sections = []
		structure = {}
		for i in self.structure:
			section = self.structure[i][0]
			while section in loadedSections:
				k = loadedSections.index(section)

				s = originalSections.pop(k)
				loadedSections.pop(k)

				sections.append(s)

			structure[section] = self.structure[i][1]

		for section in sections:
			option = ''
			options = self._config.options(section)
			items = self._config.items(section)

			if '.' in section:
				section, option = section.split('.')

			if structure.has_key(section):
				structure[section](
					section = section,
					config  = self._config,
					option  = option,
					items   = self._itemsToDict(items),
					options = options,
				)

	def _itemsToDict(self, items):
		dict = {}
		for item in items:
			dict[item[0]] = item[1]
		return dict

	def run(self):
		self.viewer.start()
		self.quit()

	def setApp(self, **params):
		for item in params['items']:
			self.__dict__[item] = params['items'][item]

	def setGrid(self, **params):
		self.grid = grid.Grid()
		items = params['items']

		if items.has_key('width') and items.has_key('height'):
			self.grid.setSize([int(items['width']), int(items['height'])])

	def setViewer(self, **params):
		items = params['items']

		try:
			viewerName = items.pop('viewer')
			exec('import viewers.'+viewerName+' as Viewer')
		except:
			raise Exception('Can\'t load viewer '+viewerName, sys.exc_info())

		self.viewer = Viewer()
		self.viewer.grid = self.grid

		if items.has_key('cellsize'):
			self.viewer.setSizeByCell(int(items.pop('cellsize')))

		# convert strings in list to integers
		self.viewer.bg = [int(i) for i in items['bg'].split(',')]

		if items.has_key('drawgrid'):
			if items['drawgrid'].lower()=="true":
				self.viewer.drawGrid = True



	def setObject(self, **params):
		name = params['option']
		objectType = params['items'].pop('type')

		try:
			exec('import objects.'+objectType+' as Object')
		except:
			raise Exception('Can\'t load object type '+objectType, sys.exc_info())

		object = Object(grid=self.grid)

		if params['items'].has_key('image'):
			object.setImage(path.join(self.images_dir, params['items'].pop('image')))
		if params['items'].has_key('position'):
			pos = params['items'].pop('position')

			if pos=="random":
				pos = self.grid.randomPosition()
			else:
				x, y = pos.split(',')

				if x=="max":
					x = self.grid.getSize()[0]-1
				if y=="max":
					y = self.grid.getSize()[1]-1
				pos = (int(x), int(y))

			self.grid.teleport(object, pos)
			self.grid.Timer.addChange(pos)
			object.position = pos

		print object.getPosition()
		self._objects[name] = object




	def setCollision(self, **params):
		pass

	def setControl(self, **params):
		controlName = params['items']['control'] or params['control']

		try:
			exec('import controls.'+controlName+' as Control')
		except:
			raise Exception('Can\'t load control '+controlName, sys.exc_info())

		c = Control(self)

		if params['items'].has_key('object'):
			c.setObject(params['items']['object'])

		self.viewer.events.update(c.getList())

	def quit(self):
		self.viewer.stop()
		try:
			self.grid.tTimer.cancel()
		except:
			pass
