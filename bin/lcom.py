# lcom command listing utility

from lib.utils import *

def _help():
    usage = '''Usage: help [options]

-h            Print this help
-a            Print all commands
              along with hidden ones.
-s (char)     Print commands starting
              with (char).'''
    print(usage)

def main(argv):
    if '-h' in argv:
        _help()
        return

    f = get_func_list()

    #check if print hidden commands
    if '-a' in argv:
        argv.remove('-a')
        # append hidden commands
        H = ' <H>'
        f.append('set' + H)
        f.append('fwd' + H)
        #sort at last
        f.sort()

    if '-s' in argv:
        # The shell doesnt send the
        # command name in the arg list
        # so the next line is not needed
        # anymore
        # argv.pop(0)#remove com name
        argv.pop(0)  #remove arg
        try:
            arg =argv[0]
            if arg.isupper():
                arg = arg.lower()
            print('Section:', arg.upper())
            for i in f:
                if i[0]==arg:
                    print('    ==>',i)
            return
        except IndexError:
            _help()
            return
        
    last='a'
    for i in f:
        if i[0] != last:
            last = i[0]
            print('Section:', last.upper())
        print('    ==>',i)
