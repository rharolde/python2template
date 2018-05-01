#!/usr/bin/env python2

''' one-line description QQQQ

(Note blank line above for docstring)
title QQQQ
Version QQQQ
Copyright (C) QQQQ
Author QQQQ
Date QQQQ

Description QQQQ

python2template
Replace all occurances of QQQQ
with the appropriate information

This template passes pylint

2018/04/11  rharolde@umich.edu
todo:
config file using configparser
'''

#from pprint import pprint
#import argparse
#import configparser
import configargparse

# SETTINGS
__progname__ = 'python2template'
__version__ = '0.2'
CONFIG_FILE = '.python2template.ini'

# DEFINE GLOBAL VARIABLES

def debug(debug_type, msg):
    '''if debugflags[debug_type] is set, then print msg'''
    if debug_type in options.debugflags:
        print msg

def python2template():
    '''docstring for python2template function QQQQ'''

    # READ COMMAND LINE AND CONFIG FILE
    config = configargparse.ArgParser(default_config_files=[CONFIG_FILE])
    config.add('--configfile', is_config_file=True, help='config file path')
    config.add('-d', '--debug', dest='debugflags', action='append',
               help='print debug messages of type DEBUG, valid types are: verbose')
    config.add('--version', action='version', version=__progname__ + ".py " + __version__)
    global options  # used in debug function
    options = config.parse_args()
    if not options.debugflags:
        options.debugflags = [] # default to empty list rather than None

    # MAIN
    debug('verbose', 'verbose mode')
    print 'do something QQQQ'
    if options.debugflags:
        print 'debug flags:'
        for flag in options.debugflags:
            print flag

if __name__ == "__main__":
    python2template()
