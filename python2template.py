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
verbose
quiet
config file using configparser
'''

import argparse

__version__ = '0.1'
PARSER = argparse.ArgumentParser()
PARSER.add_argument('--version', action='version', version='%(prog)s ' + __version__)
PARSER.parse_args()

def main():
    '''docstring for main QQQQ'''
    print 'do something QQQQ'

if __name__ == "__main__":
    main()
