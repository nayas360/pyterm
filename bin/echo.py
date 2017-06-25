# echo function
from lib.utils import make_s, prop

def _help():
    usage = '''
Usage: echo [options] <string>

[options]:
-h                Print this help.
-globals          Global vars in the
                  string will be
                  repaced with its
                  values.
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

    # if usage of global vars is enabled
    if '-globals' in argv:
        argv.remove('-globals')
        if argv == []:
            _help()
            return
        # search and replace vars wid values
        for i in range(len(argv)):
            if argv[i] in prop.vars():
                # print(i,argv[i])
                var = argv[i]
                argv.pop(i)
                argv.insert(i, prop.get(var))
    # make the string
    s = make_s(argv)

    if s == '.':
        s = ' '
    print(s)