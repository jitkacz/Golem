#!/usr/bin/env python
#-*- coding:utf-8 -*-

VERSION             = "0.1"
DATE                = "20100717"
NAME                = 'Golem Framework'
DESCRIPTION			= "Golem is Python game framework for 2D stategies, arcades etc."

SUPPORTED_LANGUAGES = ['English', 'Czech']

# names of all contributers, using 'u' for unicode encoding
JK   = {'name': u'Juda Kaleta', 'email': 'juda.kaleta@gmail.com'}
DS   = {'name': u'Daniel Švec', 'email': 'svecdaniel@centrum.cz'}

#credits
CREDITS = {
    'code'          : [JK, DS],
#   'documentation' : [OG, JT, HMC],
#   'translation'   : [HMC, OG],
}

SETUP   = {
    'name'              : NAME,
    'version'           : VERSION,
    'author'            : JK['name'] + ' and others',
    'author_email'      : JK['email'],
    'maintainer'        : JK['name'],
    'maintainer_email'  : JK['email'],
    'url'               : 'http://golem.github.com/Golem/',
    'license'           : 'Python Software Foundation License',
	'description'	    : 'Python game framework',
	'long_description'  : DESCRIPTION,


# see http://pypi.python.org/pypi?%3Aaction=list_classifiers
    'classifiers'       : [
'Development Status :: 3 - Alpha',
'Intended Audience :: Developers',
'Intended Audience :: Education',
'Intended Audience :: End Users/Desktop',
'License :: OSI Approved :: Python Software Foundation License',
'Operating System :: OS Independent',
'Operating System :: Microsoft :: Windows',
'Operating System :: POSIX :: Linux',
'Programming Language :: Python',
'Topic :: Games/Entertainment',
'Topic :: Software Development',
'Topic :: Software Development :: Build Tools',
'Topic :: Software Development :: Libraries :: Python Modules',
							] +
							['Natural Language :: ' + language for language in SUPPORTED_LANGUAGES
							],
}

