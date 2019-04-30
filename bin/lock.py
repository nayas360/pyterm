# test lock shell
from lib.pwd import chpwd, lock


def _help():
    usage = '''
Usage: lock [options]
[options]:
-h            Print this help
-chpass       Change password
'''
    print(usage)


def main(argv):
    if '-h' in argv:
        _help()
        return
    # The shell doesnt send the
    # command name in the arg list
    # so the next line is not needed
    # anymore
    # argv.pop(0)
    if '-chpass' in argv:
        chpwd()
        return
    lock()
