#!/usr/bin/bash

if [ $1 ]; then
	PYTHONPATH="/usr/lib/python2.6:./golem/" testoob --html tests.html ./golem/tests/$1
else
	PYTHONPATH="/usr/lib/python2.6:./golem/" testoob --html tests.html ./golem/tests/__init__.py
fi
