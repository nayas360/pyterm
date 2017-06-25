# ren rename command
from bin.common import *


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
    argv.pop(0)
    args = get_args(argv)
    # print(args)
    if len(args) < 2:
        _help()
        return
    old = get_path() + args[0]
    new = get_path() + args[1]
    try:
        os.rename(old, new)
    except OSError:
        print('Error[2]: "', old, '" not found', sep='')
