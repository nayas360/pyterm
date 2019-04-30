#!/usr/bin/python3

# Shell prototype
from lib.core import *

# The code segment below is for
# setting up the path in android

# Generally it should be in this path
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
