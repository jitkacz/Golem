#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

from golem import golem
from golem.libs.i18n import lang
 
print ">> Show version in default language:"
print golem.version(), "\n"

print ">> Change language to en"
lang.change('en')
print golem.version(), "\n"

print ">> Change language to cs"
lang.change('cs')
print golem.version(), "\n"

