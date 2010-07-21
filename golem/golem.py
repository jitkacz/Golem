#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os

from libs.i18n import *

__name__ = 'Golem'
__version__ = '0.1 alpha'

__doc__ = _('''
Golem is Python's game framework for developing and learning.
''')

def version():
	return _('Version of Golem is ')+__version__
