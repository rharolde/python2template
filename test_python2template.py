#!/usr/bin/env python2

''' test_python2template.def
using pytest
'''

import python2template
import re

mypackage=python2template

docstring=mypackage.__doc__

def test_docstring():
    assert docstring

def test_copyright():
    ans=False
    b=re.search(r'copyright',docstring, re.IGNORECASE)
    if b:
        ans=True
    b=re.search(r'\(c\)',docstring, re.IGNORECASE)
    if b:
        ans=True
    assert ans

def test_author():
    b=re.search(r'author',docstring, re.IGNORECASE)
    assert b

def test_date():
    b=re.search(r'date',docstring, re.IGNORECASE)
    assert b
