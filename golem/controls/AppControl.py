#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

import pygame
import controls.BaseControl

class AppControl(controls.BaseControl):
	def setEvents(self):
		self.events = {
			'onQuit' : self.quit,
		}

	def quit(self, **params):
		self.app.quit()


