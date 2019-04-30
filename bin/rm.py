# rm remove/delete command

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

    path = get_path() + '/' + make_s(argv)
    try:
        if os.listdir(path[:-len(os.path.basename(path))]) in (os.listdir('lib'), os.listdir('bin'), os.listdir()):
            err(2)
            return
    except:
        pass
    try:
        os.remove(path)
    except OSError:
        try:
            os.rmdir(path)
        except OSError:
            err(2, add=argv[0] + ' could not be deleted')
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
