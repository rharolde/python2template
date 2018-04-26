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
command line parameters using argparse
debug
config file using configparser
'''

import argparse

__version__ = '0.1'
PARSER = argparse.ArgumentParser()
PARSER.add_argument('--version', action='version', version='%(prog)s ' + __version__)
PARSER.add_argument('-d', '--debug', dest='debugflags', action='append', help='print debug messages of type DEBUG, valid types are: verbose')
args = PARSER.parse_args()
debugflags = args.debugflags
if not debugflags:
    debugflags = []

def debug(type,msg):
    '''if debugflags[type] is set, then print msg'''
    if type in debugflags:
        print msg

def main():
    '''docstring for main QQQQ'''
    debug('verbose','verbose mode')
    print 'do something QQQQ'

if __name__ == "__main__":
    main()
