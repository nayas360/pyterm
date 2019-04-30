# move command to move files only
from lib.utils import *


def _help():
    usage = '''
Usage: move (from) (to)

where (from) (to)
are valid paths.

use '%' in front of global
vars to  use  their values.
'''
    print(usage)


def main(argv):
    if len(argv) < 2 or '-h' in argv:
        _help()
        return

    args = get_args(argv)
    # The shell does the work of replacing
    # vars already. Code segment below
    # is not required anymore.
    # args = replace_vars(args)

    try:
        _from = get_path() + args[0]
        _to = get_path() + args[1]
    except IndexError:
        _help()
        return
    if os.path.isdir(_from):
        err(2, add='cant move a directory')
        return
    if os.path.isfile(_to):
        err(2, add='cant move into a file')
        return
    # print(_from,_to)
    try:
        with open(_from) as f:
            data = f.readlines()
    except IOError:
        err(2, add='"' + os.path.basename(_from) + '" coud not be moved')
        return

    try:
        with open(_to + '/' + os.path.basename(args[0]), 'w') as f:
            [print(i, file=f) for i in data]
    except IOError:
        err(2, add='"' + os.path.basename(_from) + '" could not be moved')
        return
    os.remove(_from)
