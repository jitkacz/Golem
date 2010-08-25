#!/usr/bin/env python
#-*- coding:utf-8 -*-

import objects.BaseObject

class TextIntObject(objects.BaseObject):
	text = ''
	value = 0

	def __setattr__(self, name, value):
		if name=='value':
			self.value = int(value)
			return

		self.__dict__[name] = value

	def getText(self):
		return self.text % self.value
