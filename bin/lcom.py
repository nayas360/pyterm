# lcom command listing utility

from bin.common import *


def _help():
    usage = '''
Usage: help [options]

-h            Print this help
-s (char)     Print Commands starting
              with (char).'''
    print(usage)


def main(argv):
    if '-h' in argv:
        _help()
        return

    f = func_list()
    if '-s' in argv:
        argv.pop(0)  # remove com name
        argv.pop(0)  # remove arg
        arg = make_s(argv)
        if arg.isupper():
            arg = arg.lower()
        print('Section:', arg.upper())
        for i in f:
            if i[0] == arg:
                print('    ==>', i)

        return

    last = 'a'
    for i in f:
        if i[0] != last:
            last = i[0]
            print('Section:', last.upper())
        print('    ==>', i)


def func_list():
    func = os.listdir('bin/')
    for i in range(len(func)):
        func[i] = func[i][:-3]
    rem = ['__init__',
           '__pycach',
           'core',
           'common',
           '.conf',
           '.last_tmp']
    for i in rem:
        try:
            func.remove(i)
        except ValueError:
            continue
    return sorted(func)
