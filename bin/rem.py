# rem remarks

def _help():
    usage = '''
Usage: rem <remarks>

-h            print this help
'''
    print(usage)


def main(argv):
    # rem just checked for -h
    # argv.pop(0) was never required
    if '-h' in argv:
        _help()
