# python2template
template for Python 2 scripting with boilerplate, initial tests, arguments, and config file

Notes: using configargparse

'argparse' works reasonably, but 
'configparse' requires a [section] header in the config file, which I do not want to require.  It also does not handle options that can be used multiple times ('append' in argparse).
'configargparse' looks like a good replacement, see its "Design Notes" for comparison to similar modules.
'docopt' is also interesting, but not as complete as configargparse.
