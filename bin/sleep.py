# sleep command
from bin.common import *

def _help():
    usage = '''
Usage: sleep (int)

shell sleeps for (int) time
in seconds

-h            Print this help
'''
    print(usage)

def main(argv):
    if len(argv) < 2 or '-h' in argv:
        _help()
        return
    argv.pop(0)
    try:
        t = int(make_s(argv))
        sleep(t)
    except ValueError:
        print('"', make_s(argv), '" is not a valid time interval', sep='')
