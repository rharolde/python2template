#!/usr/bin/env python2

''' test_python2template.def using pytest

last test should fail until all QQQQ entries are replaced
this passes pylint
'''

import os
import re
import subprocess
import importlib

PACKAGENAME = 'python2template'
MYPACKAGE = importlib.import_module(PACKAGENAME)
DOCSTRING = MYPACKAGE.__doc__


def test_docstring():
    '''check that docstring exists'''
    assert DOCSTRING


def test_copyright():
    '''check that copyright exists, with written out or shorthand'''
    ans = False
    result = re.search(r'copyright', DOCSTRING, re.IGNORECASE)
    if result:
        ans = True
    result = re.search(r'\(c\)', DOCSTRING, re.IGNORECASE)
    if result:
        ans = True
    assert ans


def test_author():
    '''check that author line exists'''
    result = re.search(r'author', DOCSTRING, re.IGNORECASE)
    assert result


def test_date():
    '''check that date exists'''
    result = re.search(r'date', DOCSTRING, re.IGNORECASE)
    assert result


def test_description():
    '''check that desciption exists'''
    result = re.search(r'description', DOCSTRING, re.IGNORECASE)
    assert result


def test_version():
    '''check that version exists'''
    result = re.search(r'version', DOCSTRING, re.IGNORECASE)
    assert result


def test_run():
    '''check that program runs and outputs correctly'''
    output = subprocess.check_output("./" + PACKAGENAME + ".py")
    assert output == "do something QQQQ\n"


def test_help():
    '''check -h'''
    output = subprocess.check_output(["./" + PACKAGENAME + ".py", "-h"])
    result = re.search(r'usage', output, re.IGNORECASE)
    assert result


def test_help_long():
    '''check --help'''
    output = subprocess.check_output(["./" + PACKAGENAME + ".py", "--help"])
    result = re.search(r'usage', output, re.IGNORECASE)
    assert result


def test_unrecognized_arg():
    '''test an argument that is not defined
    should get no stdout, error on stderr, and non-zero return code'''
    proc = subprocess.Popen(
        ["./" + PACKAGENAME + ".py", "--unrecognized_arg"],
        bufsize=4096,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    returncode = proc.wait()
    assert returncode == 2
    stdout, stderr = proc.communicate()
    assert stdout == ''
    result = re.search(r'unrecognized argument', stderr, re.IGNORECASE)
    assert result


def test_version_option():
    '''check --version'''
    output = subprocess.check_output(["./" + PACKAGENAME + ".py", "--version"],
                                     stderr=subprocess.STDOUT)
    result = re.search(PACKAGENAME + '.py ' + MYPACKAGE.__version__, output,
                       re.IGNORECASE)
    assert result


def test_debug():
    '''check debug config option'''
    output = subprocess.check_output(["./" + PACKAGENAME + ".py", "-d",
                                      "config"])
    assert 'Command Line Args:   -d config' in output
    assert 'config mode' in output



def test_debug_long():
    '''check debug long option'''
    output = subprocess.check_output(["./" + PACKAGENAME + ".py", "--debug",
                                      "config"])
    assert 'Command Line Args:   --debug config' in output


def test_verbose():
    '''check verbose option'''
    output = subprocess.check_output(["./" + PACKAGENAME + ".py", "-v"],
                                     stderr=subprocess.STDOUT)
    assert 'INFO:root:logging is at info or above' in output


def test_verbose_long():
    '''check verbose long option'''
    output = subprocess.check_output(["./" + PACKAGENAME + ".py", "--verbose"],
                                     stderr=subprocess.STDOUT)
    assert 'INFO:root:logging is at info or above' in output


def test_verbose_repeated():
    '''check repeated verbose option'''
    output = subprocess.check_output(["./" + PACKAGENAME + ".py", "-vv"],
                                     stderr=subprocess.STDOUT)
    assert 'DEBUG:root:logging is at debug or above' in output


def test_config_file_variable():
    '''check that CONFIG_FILE constant exists'''
    assert MYPACKAGE.CONFIG_FILE  # defined and not zero length



def test_default_config_file():
    '''check that default config_file is read'''
    with open(MYPACKAGE.CONFIG_FILE, 'w') as filehandle:
        filehandle.write('debug=config\n')
    output = subprocess.check_output(["./" + PACKAGENAME + ".py"])
    os.remove(MYPACKAGE.CONFIG_FILE)
    assert 'Config File (.python2template.ini):\n  debug:             config' \
        in output


def test_command_line_config_file():
    '''check that command line config_file is read'''
    output = subprocess.check_output(["./" + PACKAGENAME + ".py",
                                      "--configfile",
                                      ".python2template.ini.sample"])
    assert 'Config File (.python2template.ini.sample):' in output
    assert 'debug:             config' in output


def test_no_qqqq():
    '''check that all QQQQ have been replaced

    This test is expected to fail when starting out
    Keep this as the last test
    '''
    result = re.search(r'QQQQ', DOCSTRING)
    assert not result
