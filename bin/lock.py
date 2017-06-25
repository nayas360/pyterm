# test lock shell
import getpass
import hashlib


def _help():
    usage = '''
Usage: lock [options]
[options]:
-h            Print this help
-chpass       Change password
'''
    print(usage)


key = 'bin/lock.key'


def main(argv):
    if '-h' in argv:
        _help()
        return
    argv.pop(0)
    if '-chpass' in argv:
        ch()
        return
    lock()


def ch():
    p = '''
Unlock the shell to prove authenticity.'''
    print(p)
    lock()
    print('Authenticity Proved...')
    sleep(1)
    _reg_pass()


def lock():
    try:
        with open(key) as kw:
            data = kw.readline()
        p = '''The shell is LOCKED.'''
        print(p)
        inp = get_hash(getpass.getpass('Password: '))
        if inp in data:
            return
        else:
            print('Incorrect password !')
            lock()
    except IOError:
        p = '''
Registered password was not found.
Enter Password to register.
'''
        print(p)
        _reg_pass()


def _reg_pass():
    p = '''
You wont be able to see what
you are typing.
'''
    print(p)
    _pass = get_pass()
    with open(key, 'w') as kw:
        print(_pass, file=kw)
    print('\nPassword was registered...')


def get_pass():
    new_password = getpass.getpass('New Password: ')
    if len(new_password) < 4:
        p = '''Password must be atleast 4 characters
long...
'''
        print(p)
        return get_pass()
    confirm_password = getpass.getpass('Confirm Password: ')
    if new_password == confirm_password:
        pass_key = get_hash(new_password)
        return pass_key
    else:
        print("Passwords entered doesn't match...")
        return get_pass()


def get_hash(_pass):
    _pass = bytes(_pass, 'utf-8')
    _hash = hashlib.new('sha1', _pass)
    _hash = _hash.hexdigest()
    return _hash
