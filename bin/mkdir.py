# mkdir command

from bin.common import *

def main(argv):
    if len(argv) < 1 or '-h' in argv:
        _help()
        return
    # The shell doesnt send the
    # command name in the arg list
    # so the next line is not needed
    # anymore
    # argv.pop(0)
    if make_s(argv) in ('.', '..', '-'):
        err(2, add='invalid directory name')
        return
    path = get_path() + make_s(argv)
    
    try:
        os.mkdir(path)
    except OSError:
        print('"', argv[0], '" directory already exsists', sep='')
        return
    print('"', argv[0], '" directory created', sep='')
    #print('Path:',path)

def _help():
    usage = '''Usage: mkdir (dir)
    
Where (dir) is the
    name of the new
    directory to be
    created.
'''
    print(usage)