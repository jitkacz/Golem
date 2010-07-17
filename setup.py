#!/usr/bin/env python

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
        "PyGame>=0",
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
