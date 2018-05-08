# python2template
template for Python 2 scripting with boilerplate, initial tests,
arguments, and config file

When using this template, copy these files into a new project
directory and update as needed:
python2template.py
test_python2template.py
.python2template.ini.sample
pytest.ini
.pylintrc
.gitignore
LICENSE
README.md

Run these tests to be sure it is ok:
pytest   # last test should fail until template is customize
pylint *.py
flake8 *.py


Note:  Uses configargparse.

'argparse' works well, but
'configparse' requires a [section] header in the config file, which I do not want.  It also does not handle options that can be used multiple times ('append' in argparse).
'configargparse' replaces both argparse and configparse, see its "Design Notes" for comparison to similar modules.
'docopt' is also interesting, but not as complete as configargparse.
