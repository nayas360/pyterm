# echo function
from lib.utils import make_s

def main(argv):
    if len(argv) < 1 or '-h' in argv:
        print('Usage: echo <string>')
        return
    # The shell doesnt send the
    # command name in the arg list
    # so the next line is not needed
    # anymore
    # argv.pop(0)
    s = make_s(argv)
    if s == '.':
        s = ' '
    print(s)