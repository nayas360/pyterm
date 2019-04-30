# sleep command
from time import sleep

from lib.utils import *


def _help():
    usage = '''
Usage: sleep (int)

shell sleeps for (int) time
in seconds

-h            Print this help
'''
    print(usage)


def main(argv):
    if len(argv) < 1 or '-h' in argv:
        _help()
        return
    # The shell doesnt send the
    # command name in the arg list
    # so the next line is not needed
    # anymore
    # argv.pop(0)
    try:
        t = int(make_s(argv))
        sleep(t)
    except ValueError:
        print('"', make_s(argv), '" is not a valid time interval', sep='')
