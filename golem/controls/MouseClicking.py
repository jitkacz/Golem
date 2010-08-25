#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pygame

import controls.BaseControl


class MouseClicking(controls.BaseControl):
	def setEvents(self):
		self.events = {
			'onButtonUp' :  self.onButtonUp,
			'onButtonDown' : self.onButtonDown,
		}

	def onButtonUp(self, **params):
		pass

	def onButtonDown(self, **params):
		pass
