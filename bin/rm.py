# rm remove/delete command

from bin.common import *


def main(argv):
    if len(argv) < 2 or '-h' in argv:
        _help()
        return
    argv.pop(0)
    path = get_path() + '/' + make_s(argv)
    try:
        os.remove(path)
    except OSError:
        try:
            os.rmdir(path)
        except OSError:
            print('Error[5]: "', argv[0], '" could not be deleted', sep='')
            return
        print('"', argv[0], '" directory has been deleted', sep='')
        return
    print('"', argv[0], '" file has been deleted', sep='')


def _help():
    usage = '''Usage: rm [(dir)/(file)]
    
Where [(dir)/(file)] 
    is the name of the
    directory/file to be
    removed/deleted.
'''
    print(usage)
