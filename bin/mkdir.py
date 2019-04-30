# mkdir command

from lib.utils import *


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

    if make_s(argv) in ('.', '..', '-'):
        err(2, add='invalid directory name')
        return
    path = get_path() + make_s(argv)
    try:
        if os.listdir(path[:-len(os.path.basename(path))]) in (os.listdir('lib'), os.listdir('bin'), os.listdir()):
            err(2)
            return
    except:
        pass

    try:
        os.mkdir(path)
    except OSError:
        print('"', argv[0], '" directory already exsists', sep='')
        return
    print('"', argv[0], '" directory created', sep='')
    # print('Path:',path)


def _help():
    usage = '''Usage: mkdir (dir)
    
Where (dir) is the
    name of the new
    directory to be
    created.

Use '%' in front of
global vars to use
their value as dir name.
'''
    print(usage)
