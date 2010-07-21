#!/usr/bin/env python

import os

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
		'golem.libs.test',
		sources = ['golem/libs/test.c'],
	),
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
	message_extractors = {'golem': [
		('**.py', 'python', None),
	]},

	ext_modules = clibs,

	**info.SETUP
)


