# Exit function
from sys import exit
from time import sleep

from lib.utils import prop, set_path
from lib.vfs import cleanup


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
    # exit gets an empty arg list
    # now, shell doesnt send the
    # comm name anymore
    if '-h' in argv:
        _help()
        return
    if '-t' in argv:
        i = argv.index('-t') + 1
        try:
            t = int(argv[i])
            die(t)
        except ValueError:
            print('"', argv[i], '" is not a valid time interval...', sep='')
            print('Exiting with default time...')
        except IndexError:
            print('You forgot to give the time...')
            print('Exiting with default time...')
    die()


def die(t=2):
    print('Stopping Shell...')
    sleep(1)
    print('Closed Everything...')
    print('will exit in', t, 'seconds...')
    sleep(t)
    if prop.get('save_state') == '0':
        set_path('root/')
        prop.set('prompt', '-def')
    cleanup()
    exit()
