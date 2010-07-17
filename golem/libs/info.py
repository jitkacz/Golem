#!/usr/bin/env python
#-*- coding:utf-8 -*-

VERSION             = "0.1"
DATE                = "20100717"
NAME                = 'Golem'
GPL_VERSION         = '2'
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
    'url'               : '',
    'license'           : 'GNU GPL v.' + GPL_VERSION,
	'description'	   : 'Python game framework',
	'long_description'  : "Golem is Python game framework for 2D stategies, arcades etc.",


# see http://pypi.python.org/pypi?%3Aaction=list_classifiers
    'classifiers'       : [
                           'Development Status :: 3 - Alpha',
                           'Environment :: X11 Applications',
                           'Environment :: X11 Applications :: GTK',
                           'Intended Audience :: End Users/Desktop',
                           'License :: OSI Approved :: GNU General Public License (GPL)',
                           'Operating System :: OS Independent',
                           'Operating System :: POSIX :: Linux',
                           'Programming Language :: Python',
						   ] +
                          ['Natural Language :: ' + language for language in SUPPORTED_LANGUAGES
                          ],
}

