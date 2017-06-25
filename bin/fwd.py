# forward commands to the host system
from lib.utils import *


def _help():
    usage = '''
Usage: fwd (command)

Where command is a valid
host system command.
'''
    print(usage)


def main(argv):
    if len(argv) == 0 or '-h' in argv:
        _help()
        return

    from os import system
    system(make_s(argv))
