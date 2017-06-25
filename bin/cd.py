# cd change directory command
from bin.common import *


def _help():
    usage = '''Usage: cd (path)

Where (path) refers to the
path to where directory has
to be changed to.

use -cur as argument
to JUST print the
current path.
'''
    print(usage)


def main(argv):
    if len(argv) < 2 or '-h' in argv:
        _help()
        return
    argv.pop(0)

    if '..' in argv and get_path() == 'root/':
        err(2, add='Cant cd back from root/')
        return
    elif '..' in argv and get_path() != 'root/':
        path = get_prv_path()
        goto(path)
        return
    if '-cur' in argv:
        path = get_path()
        print('Path:', path)
        return

    if './' in argv:
        path = 'root/'
        goto(path)
        return
    path = get_path() + make_s(argv)
    if make_s(argv)[-1] != '/':
        path = get_path() + make_s(argv) + '/'
    try:
        if make_s(argv) in os.listdir(get_path()) or get_last_path(path) in os.listdir(get_prv_path2(path)):
            goto(path)
            return
        else:
            err(2, path[:-1])
            return
    except OSError:
        err(2, path[:-1])


def goto(path):
    if os.path.isfile(path[:-1]):
        err(2, add='Cant cd into a file')
        return
    set_path(path)
    # print('Path:',path)
