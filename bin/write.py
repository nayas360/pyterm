# write function
from lib.utils import *


def _help():
    usage = '''
Usage: write (filename)

if (filename) exists inputs
will be appended else a new 
file will be created.

-h            Print this help
-r            Overwrite the 
              original file.
              All data is lost.

Use '%' in front of global
vars to use the value as
the file name.

While in write mode use
"-exit" to exit write mode
"-show" to see file contents
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

    # replace the vars
    # The shell does the work of replacing
    # vars already. Code segment below
    # is not required anymore.
    # argv = replace_vars(argv)

    if '-r' in argv:
        argv.pop(0)
        path = get_path() + make_s(argv)
        try:
            with open(path, 'w') as f:
                pass
            print('Writing over "', make_s(argv), '" file', sep='')
        except IOError:
            err(3, add='Cant write into a directory')
            return

    path = get_path() + make_s(argv)
    s = 'write>'
    try:
        with open(path, 'a') as f:
            while True:
                inp = input(s)
                if '-exit' in inp:
                    break
                elif '-show' in inp:
                    f.close()
                    _show(path)
                    f = open(path, 'a')
                else:
                    print(inp, file=f)
    except IOError:
        err(3, add='Cant write into a directory')


def _show(path):
    with open(path) as f:
        data = f.readlines()
    print('_________________<START>_________________\n')
    print(make_s2(data))
    print('__________________<END>__________________\n')
