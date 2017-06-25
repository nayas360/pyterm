# type command prints file contents
from bin.common import *


def _help():
    usage = '''
Usage: type (file)
'''
    print(usage)


def main(argv):
    if len(argv) < 2 or '-h' in argv:
        _help()
        return
    argv.pop(0)

    path = get_path() + make_s(argv)
    if os.path.isfile(path):
        with open(path) as f:
            data = f.readlines()
        print('_________________<START>_________________\n')
        print(make_s2(data))
        print('__________________<END>__________________\n')
        return
    print('Error[4]: "', path, '" could not be opened', sep='')
