# echo function
from bin.common import make_s


def main(argv):
    if len(argv) < 2 or '-h' in argv:
        print('Usage: echo <string>')
        return
    argv.pop(0)
    s = make_s(argv)
    if s == '.':
        s = ' '
    print(s)
