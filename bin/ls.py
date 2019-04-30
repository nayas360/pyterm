# ls command
from lib.utils import *


def _help():
    usage = '''
Usage: ls [options] [dir]

[options]:
-a              shows all files
                including hidden
                ones
[dir]           lists items in (dir)
                directory

Use '%' in front of global vars
to use this value as for name.'''
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

    if len(argv) != 0:  # '-d' in argv:
        # The shell doesnt send the
        # command name in the arg list
        # so the next line is not needed
        # anymore
        # argv.pop(0)
        # argv.remove('-d')

        # The shell does the work of replacing
        # vars already. Code segment below
        # is not required anymore.
        # if '%' in make_s(argv): #in prop.vars():
        # path=get_path()+make_s(replace_vars(argv))
        # else:
        path = get_path() + make_s(argv)
    else:
        path = get_path()

    if os.path.isfile(path):
        err(2, add='Cant list a file')
        return
    try:
        if os.listdir(path) in (os.listdir('lib'), os.listdir('bin'), os.listdir()):
            err(2, path)
            return
    except OSError:
        err(2, path)
        return

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
