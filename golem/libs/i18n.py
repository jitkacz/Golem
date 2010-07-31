#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, locale, gettext

import config



__all__ = ['_', 'Lang', 'lang']

class Lang(object):
	path = ''
	lang = None
	domain = ''

	def gettext(self, string):
		return self.lang.gettext(string)

	def __init__(self, path, domain='golem'):
		self.domain = domain
		self.path = path
<<<<<<< HEAD
			
=======

>>>>>>> 5ead219ebd17b91bee4f0d293874d7b597615e63
		if os.name=='nt':
			locale.setlocale(locale.LC_ALL, '')
			self.change(locale.getdefaultlocale()[0][:2])
		else:
			self.change()

	def change(self, lang=None):
		if lang:
			self.lang = gettext.translation(self.domain, self.path, languages=[lang])
		else:
			self.lang = gettext.translation(self.domain, self.path)
		self.lang.install()
		#print self.lang._info['language-team']

lang = Lang(os.path.join(config.BASEDIR, 'locale'))
_ = lang.gettext

