#!/usr/bin/env python
#-*- coding:utf-8 -*-

import objects.BaseObject

class TextObject(objects.BaseObject):
	text = ''

	def getText(self):
		return self.text
