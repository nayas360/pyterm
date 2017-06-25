# Shell prototype
from lib.core import *

P = 'sdcard/com.hipipal.qpyplus/projects3/shell'
try:
    os.chdir(P)
except OSError:
    pass

def main():
    s = shell()
    s.start()


if __name__ == '__main__':
    os.system('clear')
    main()
