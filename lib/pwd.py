# for sleeping
# Password routines
import getpass
import hashlib
from time import sleep

key = 'lib/lock.key'


def chpwd():
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
        inp = get_hash(getpass.getpass())
        if inp in data:
            return
        else:
            print('\nIncorrect password !')
            lock()
    except IOError:
        p = '''
Registered password was not found.
Enter Password to register.
'''
        print(p)
        _reg_pass()
        print('Now locking the shell...\n')
        lock()


def _reg_pass():
    p = '''
You wont be able to see what
you are typing.
'''
    print(p)
    _pass = get_pass()
    with open(key, 'w') as kw:
        print(_pass, sep='\n', file=kw)
    print('\nPassword was registered...')


def get_pass():
    new_password = getpass.getpass('New Password: ')
    if len(new_password) < 4:
        p = '''Password must be atleast 4 characters long...
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
