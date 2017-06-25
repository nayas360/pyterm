# Shell prototype
from bin.core import *

P = 'sdcard/com.hipipal.qpyplus/projects3/shell'
try:
    os.chdir(P)
except OSError:
    pass


def main():
    s = shell()
    s.start()


if __name__ == '__main__':
    main()
