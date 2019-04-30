# echo function
from lib.utils import make_s, prop


def _help():
    usage = '''
Usage: echo [options] <string>

[options]:
-h                Print this help.
-all              All Global vars
                  in the string will
                  be replaced with its
                  values.

Use '%' in front of vars to replace
only that var with value.
eg. echo Value of prompt is %prompt
will echo value of prompt
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

    # if usage of global vars is enabled
    if '-all' in argv:
        argv.remove('-all')
        if argv == []:
            _help()
            return
        # search and replace vars wid values
        for i in range(len(argv)):
            var = argv[i]
            if var in prop.vars():
                # print(i,argv[i])
                argv.pop(i)
                argv.insert(i, prop.get(var))

    # new algorithm for detecting global vars
    # The shell does the work of replacing
    # vars already. Code segment below
    # is not required anymore.
    # argv=replace_vars(argv)

    # make the string
    if len(argv) != 0:
        s = make_s(argv)
    else:
        # insert blanks if argv is empty
        s = ' '
    # for detecting escape sequences
    if '\\n' in s:
        s = s.replace('\\n', '\n')

    print(s)
