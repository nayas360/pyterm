# set command to set global variables
from lib.utils import *

def _help():
    usage = '''
Usage: set [options] (var) [value]

[options]:
-h                Print this help.

-del (var)        Delete variable
                  (var) if defined.

where (var) is a valid
global variable
if [value] is not given,
current value is returned
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
    # argv.pop(0) #remove arg

    # to show all vars
    if len(argv) < 1:
        for i in prop.vars():
            print(i, ' = ', prop.get(i))
        return
    if '-del' in argv:
        try:
            var = argv[1]
            #detect system vars
            if var == 'save_state':
                err(4, add='Cant delete system variable "' + var+'"')
                return
            prop.delete(var)
            return
        except IndexError:
            err(4, add='variable name was missing')
            return

    var = argv[0]

    if len(argv) < 2:
        val = prop.get(var)
        if val ==NULL:
            err(4,var)
            return
        print(val)          
        return

    #remove name of var
    argv.pop(0)
    # make the rest the val
    val = make_s(argv)
    try:
        prop.set(var,val)
    except ValueError:
        err(4, add="can't create this variable")
