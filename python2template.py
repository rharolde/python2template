#!/usr/bin/env python2

""" one-line description QQQQ

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

This template passes pylint with one change, see .pylintrc
This template passes flake8

2018/04/11  rharolde@umich.edu
todo:
"""

# double underscore names
__progname__ = 'python2template'
__version__ = '0.2'

# from pprint import pprint
import logging
import configargparse

# defaults
CONFIG_FILE = '.python2template.ini'

# define global variables


def debug(debug_type, msg):
    """if debugflags[debug_type] is set, then print msg"""
    if debug_type in options.debugflags:
        print msg


def python2template():
    """docstring for python2template function QQQQ"""
    # MAIN
    debug('config', 'config mode')
    logging.info('logging is at info or above')
    logging.debug('logging is at debug or above')
    print 'do something QQQQ'
    if options.debugflags:
        print 'debug flags:'
        for flag in options.debugflags:
            print flag
        config.print_values()


if __name__ == "__main__":
    # READ COMMAND LINE AND CONFIG FILE
    config = configargparse.ArgParser(default_config_files=[CONFIG_FILE])
    config.add('--configfile', is_config_file=True, help='config file path')
    config.add('-d', '--debug', dest='debugflags', action='append',
               help='print debug messages of type DEBUG, valid types are: \
               config')
    config.add('--version', action='version', version=__progname__ + ".py "
               + __version__)
    config.add_argument('-v', '--verbose', action='count',
                        help='can be repeated up to two times')
    options = config.parse_args()
    if not options.debugflags:
        options.debugflags = []     # default to empty list rather than None
    logger = logging.getLogger()
    if options.verbose:
        if options.verbose > 2:
            logging.warning('verbose was repeated more than two times')
            config.print_help()
        if options.verbose == 1:
            logger.setLevel(logging.INFO)
        if options.verbose == 2:
            logger.setLevel(logging.DEBUG)

    # call MAIN
    python2template()
