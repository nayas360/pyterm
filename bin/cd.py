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
        print('Error[3]: Cant go back from root/')
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
    if make_s(argv)[-1] == '/':
        path = get_path() + make_s(argv)
    else:
        path = get_path() + make_s(argv) + '/'

    if make_s(argv) in os.listdir(get_path()) or get_last_path(path) in os.listdir(get_prv_path2(path)):
        goto(path)
        return
    else:
        print('Error[2]: "', path, '" path does not exist', sep='')
        return

def goto(path):
    if os.path.isfile(path[:-1]):
        print('Error[3]: Cant cd into a file')
        return
    set_path(path)
    # print('Path:',path)
