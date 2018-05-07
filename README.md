# python2template
template for Python 2 scripting with boilerplate and initial tests
arguments and config filehandle

Notes:
'argparse' works reasonably
'configparse' requires a [section] header in the config file, which I do not want to require.  It also does not handle options that can be used multiple times ('append' in argparse).
'configargparse' looks like a good replacement, see its "Design Notes" for comparison to similar modules
'docopt' is also interesting, but not as complete as configargparse
