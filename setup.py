#!/usr/bin/env python

import os, glob

try:
    from setuptools import setup, find_packages, Extension
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages, Extension

from golem.libs import info

os_files = [
	 # man-page ("man 1 golem")
	 ('share/man/man1',['docs/golem.1']),
]

clibs = [
	Extension(
		'golem.grid.createGrid',
		sources = ['golem/grid/createGrid.c'],
	),
	Extension(
		'golem.grid.findWay',
		sources = ['golem/grid/findWay.c'],
	),
]

# Add all the translations
locale_files = []
for filepath in glob.glob("golem/locale/*/LC_MESSAGES/*"):
	filepath = filepath.replace('golem/', '')
	locale_files.append(filepath)

setup(
	zip_safe=True,
	include_package_data=True,


    install_requires=[
        "PyGame>=1.9.1",
        "NumPy>=1.4.1",
    ],

    packages=find_packages(exclude=['ez_setup']),
    scripts	= ['bin/golem'],
    package_data= {
		'golem': locale_files
	},
	message_extractors = {'golem': [
		('**.py', 'python', None),
	]},
	data_files = os_files,
	ext_modules = clibs,

	**info.SETUP
)


