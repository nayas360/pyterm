# write function
from bin.common import *

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

While in write mode use
"-exit" to exit write mode
"-show" to see file contents
'''
    print(usage)

def main(argv):
    if len(argv) < 2:
        _help()
        return

    argv.pop(0)

    if '-r' in argv:
        argv.pop(0)
        path = get_path() + make_s(argv)
        try:
            with open(path, 'w') as f:
                pass
            print('Writing over "', make_s(argv), '" file', sep='')
        except IOError:
            print('Error[4]: Cant write into a directory')

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
        print('Error[4]: Cant write into a directory')

def _show(path):
    with open(path) as f:
        data = f.readlines()
    print('_________________<START>_________________\n')
    print(make_s2(data))
    print('__________________<END>__________________\n')

