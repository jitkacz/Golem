#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import libs.info

from libs.i18n import *


__name__ = libs.info.NAME
__version__ = libs.info.VERSION

__doc__ = _('''
Golem is Python's game framework for developing and education.
''')

def version():
	return _('Version of Golem is ')+__version__
