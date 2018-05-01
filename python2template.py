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

import argparse
import configparser

# SETTINGS
__version__ = '0.2'
CONFIG_FILE = ".python2template.ini"

# READ COMMAND LINE ARGUMENTS AND OPTIONS
PARSER = argparse.ArgumentParser()
PARSER.add_argument('--version', action='version', version='%(prog)s ' + __version__)
PARSER.add_argument('-d', '--debug', dest='debugflags', action='append',
                    help='print debug messages of type DEBUG, valid types are: verbose')
ARGS = PARSER.parse_args()
DEBUG_FLAGS = ARGS.debugflags
if not DEBUG_FLAGS:
    DEBUG_FLAGS = []

# READ CONFIGURATION file
CONFIG = configparser.ConfigParser()
CONFIG.read(CONFIG_FILE)
try:
    DEBUG_CONFIG = CONFIG.get("global", "debug")
    DEBUG_FLAGS.append(DEBUG_CONFIG)
except configparser.NoOptionError:
    pass
except configparser.NoSectionError:
    pass

def debug(debug_type, msg):
    '''if DEBUG_FLAGS[debug_type] is set, then print msg'''
    if debug_type in DEBUG_FLAGS:
        print msg

def main():
    '''docstring for main QQQQ'''
    debug('verbose', 'verbose mode')
    print 'do something QQQQ'
    if DEBUG_FLAGS:
        print 'debug flags:'
        for flag in DEBUG_FLAGS:
            print flag

if __name__ == "__main__":
    main()
