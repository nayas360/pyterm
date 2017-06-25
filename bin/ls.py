# ls command
from bin.common import *


def main(argv):
    if '-h' in argv:
        usage = '''
Usage: ls [options]

[options]:
-d (dir)        lists items in (dir)
                directory'''
        print(usage)
        return
    if '-d' in argv:
        argv.pop(0)
        argv.remove('-d')
        s = get_path() + make_s(argv)
        pprint(s)
    else:
        path = get_path()
        pprint(path)


def pprint(path):
    try:
        l = os.listdir(path)
    except OSError:
        print('Error[2]: "', path, '" path does not exist', sep='')
        return
    if l == []:
        print('Empty directory')
        return
    for i in l:
        print(i)