#!/usr/bin/env python

import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

from golem.libs import info

os_files = [
	 # man-page ("man 1 golem")
	 ('share/man/man1',['docs/golem.1']),
]

setup(
	zip_safe=True,
	include_package_data=True,


    install_requires=[
        "PyGame>=1.9.1",
    ],

    packages=find_packages(exclude=['ez_setup']),
    scripts	= ['bin/golem'],
    package_data= {
		'golem': [
			'golem/*.py',
			'golem/locale/*/LC_MESSAGES/*.mo',
			]
	},
	**info.SETUP
)

def removeDir(name):
	try:
		os.rmdir(name)
	except:
		for i in os.listdir(name):
			path = os.path.join(name, i)
			print "removing: "+path
			if os.path.isfile(path):
				os.remove(path)
			else:
				removeDir(path)
				try:
					os.rmdir(path)
				except:
					pass
		os.rmdir(name)

try:
	removeDir('build')
	removeDir('Golem.egg-info')
except:
	pass

