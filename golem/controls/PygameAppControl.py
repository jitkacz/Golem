#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

import pygame
import controls.BaseControl

class PygameAppControl(controls.BaseControl):
	def setEvents(self):
		self.events = {
			pygame.QUIT : self.quit
		}

	def quit(self):
		self.app.quit()


