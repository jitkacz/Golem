#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys

for file in os.listdir('./golem/tests/'):
	if ('.' in file) and file!="__init__.py":
		name, ext = file.split('.')
		if ext=="py":
			try:
				exec("from "+name+" import *")
			except:
				pass

