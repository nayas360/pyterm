# mkdir command

from bin.common import *

def main(argv):
    if len(argv) < 2 or '-h' in argv:
        _help()
        return
    argv.pop(0)

    path = get_path() + make_s(argv)

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
'''
    print(usage)