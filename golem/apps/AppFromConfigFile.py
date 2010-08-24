#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

import apps.BaseApp
import ConfigParser

import grid.Grid

class AppFromConfigFile(apps.BaseApp):
	_config = None

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
		pass

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
			exec('import viewers.'+viewerName+' as viewer')
		except:
			raise Exception('Can\'t load viewer '+viewerName)

		self.viewer = viewer()
		self.viewer.grid = self.grid

		if items.has_key('cellsize'):
			self.viewer.setSizeByCell(int(items.pop('cellsize')))

		# convert strings in list to integers
		self.viewer.bg = [int(i) for i in items['bg'].split(',')]


	def setObject(self, **params):
		pass

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
