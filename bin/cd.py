# cd change directory command
from lib.utils import *


def _help():
    usage = '''Usage: cd (path)

Where (path) refers to the
path to where directory has
to be changed to.

use '%' in front of global
variables to pass their
values.

use -cur as argument
to JUST print the
current path.
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
        if get_path() == 'root/':
            print('Already in root/')
            return
        path = 'root/'
        goto(path)
        return
    path = get_path() + make_s(argv)
    try:
        if make_s(argv) in os.listdir(get_path()) or get_last_path(path) in os.listdir(get_prv_path2(path)):
            goto(path)
            return
            # The shell does the work of replacing
            # vars already. Code segment below
            # is not required anymore.
            # elif '%' in  make_s(argv): #in prop.vars():
            # arg=prop.get(make_s(argv))
            # arg=replace_vars(argv)
            # path=get_path()+make_s(arg)
            # if arg in os.listdir(get_path()) or get_last_path(path) in os.listdir(get_prv_path2(path)):
            # goto(path)
            # return
            # else:
            # err(2,path)
            # return
        else:
            err(2, path)
            return
    except OSError:
        err(2, path[:-1])


def goto(path):
    if os.path.isfile(path):
        err(2, add='Cant cd into a file')
        return
    if os.listdir(path) in (os.listdir('lib'), os.listdir('bin'), os.listdir()):
        err(2, path)
        return
    set_path(path)
    # print('Path:',path)
