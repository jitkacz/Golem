#!/usr/bin/env bash

if [ $1 ]; then
	PYTHONPATH="/usr/lib/python2.6:./golem/" testoob  ---coverage=massive --pdf tests.pdf ./golem/tests/$1
else
	PYTHONPATH="/usr/lib/python2.6:./golem/" testoob -v --coverage=massive --pdf tests.pdf ./golem/tests/__init__.py
fi
