# ren rename command
from lib.utils import *


def _help():
    usage = '''
Usage: ren (old) (new)

(old)=> old name of file/directory
(new)=> new name of file/directory

-h            Print this help
'''
    print(usage)


def main(argv):
    if '-h' in argv:
        _help()
        return
    # The shell doesnt send the
    # command name in the arg list
    # so the next line is not needed
    # anymore
    # argv.pop(0)
    args = get_args(argv)
    # The shell does the work of replacing
    # vars already. Code segment below
    # is not required anymore.
    # args=replace_vars(args)
    # print(args)
    if len(args) < 2:
        _help()
        return
    old = get_path() + args[0]
    new = get_path() + args[1]
    try:
        os.rename(old, new)
    except OSError:
        err(2, add=old + ' not found')
