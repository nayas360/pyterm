# rem remarks

def _help():
    usage = '''
Usage: rem <remarks>

-h            print this help
'''
    print(usage)


def main(argv):
    if '-h' in argv:
        _help()
