# Exit function
from bin.common import sleep
from sys import exit


def _help():
    usage = '''
Usage: exit [options]

[options]:
-t (int)        exits after (int)
                time in seconds.

-h              Print this help.
'''
    print(usage)


def main(argv):
    if '-h' in argv:
        _help()
        return
    if '-t' in argv:
        i = argv.index('-t') + 1
        try:
            t = int(argv[i])
            print('Stopping Shell...')
            sleep(1)
            print('Closed Everything...')
            print('will exit in', t, 'seconds...')
            sleep(t)
            exit()
        except ValueError:
            print('"', argv[i], '" is not a valid time interval...', sep='')
            print('Exiting with default time...')
        except IndexError:
            print('You forgot to give the time...')
            print('Exiting with default time...')
    print('Stopping Shell...')
    sleep(1)
    print('Closed Everything...')
    print('will exit in 2 seconds...')
    sleep(2)
    exit()
