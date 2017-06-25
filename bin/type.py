# type command prints file contents
from bin.common import *

def _help():
    usage = '''
Usage: type (file)

print content of (file)
'''
    print(usage)

def main(argv):
    if len(argv) < 2 or '-h' in argv:
        _help()
        return
    argv.pop(0)
    argv = make_s(argv)

    path = get_path() + argv
    if os.path.isfile(path):
        with open(path) as f:
            data = f.readlines()
        print('_________________<START>_________________\n')
        print(make_s2(data))
        print('__________________<END>__________________\n')
        return
    elif os.path.isdir(path):
        err(3, add=argv + ' is a directory')
    else:
        err(2, path)
