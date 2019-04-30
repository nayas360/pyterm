# type command prints file contents
from lib.utils import *


def _help():
    usage = '''
Usage: type (file)

Print content of (file)

Use '%' in front of global
vars to use value as file
name.

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

    # The shell does the work of replacing
    # vars already. Code segment below
    # is not required anymore.
    # argv=replace_vars(argv)
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
