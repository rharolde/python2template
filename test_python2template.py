#!/usr/bin/env python2

''' test_python2template.def
using pytest
'''

import python2template

print(python2template.__doc__)

def chkdocstring():
    return python2template.__doc__

def test_chkdocstring():
    assert chkdocstring()


'''
def foo():
    doc = "The [object Object] property."
    def fget(self):
        return self._[object Object]
    def fset(self, value):
        self._[object Object] = value
    def fdel(self):
        del self._[object Object]
    return locals()
 = property(**())
'''
