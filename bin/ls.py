# ls command
from bin.common import *


def _help():
    usage = '''
Usage: ls [options]

[options]:
-a              shows all files
                including hidden
                ones
-d (dir)        lists items in (dir)
                directory'''
    print(usage)


def main(argv):
    if '-h' in argv:
        _help()
        return

    if '-a' in argv:
        argv.remove('-a')
        ALL = True
    else:
        ALL = False

    if '-d' in argv:
        argv.pop(0)
        argv.remove('-d')
        path = get_path() + make_s(argv)
    else:
        path = get_path()

    if ALL:
        pprint(path)
    else:
        pprint2(path)


def pprint(path):
    try:
        l = os.listdir(path)
    except OSError:
        err(2, path)
        return
    if l == []:
        print('Empty directory')
        return
    for i in sorted(l):
        print(i)


def pprint2(path):
    try:
        l = os.listdir(path)
    except OSError:
        err(2, path)
        return
    if l == []:
        print('Empty directory')
        return
    for i in sorted(l):
        if i[0] == '.':
            continue
        print(i)
