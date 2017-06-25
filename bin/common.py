# commons imports

import os
import configparser as cp
from time import sleep


# String manipulators____________________
def make_s(l):
    __doc__ = '''
    Makes a sentence with spaces
    in between from a list of
    strings.
    returns a string.'''
    s = str()
    for i in l:
        s += i + ' '
    s = s[:-1]
    return s


def make_s2(l):
    __doc__ = '''
    Makes a sentence from a
    list of strings.
    returns a string.'''
    s = str()
    for i in l:
        s += i
    s = s[:-1]
    return s


# Error definitions______________________
def err(n, inp=None, add=None):
    # shell error
    if n == 0:
        if inp != None:
            print('Error[0]: "', inp, '" was not recognised as a command or an expression', sep='')
        elif add != None:
            print('Error[0]:', add)
        else:
            print('Error[0]: invalid command or expression')
        return
    # shell error
    elif n == 1:
        if inp != None:
            print('Error[1]: "', inp, '" command could not be executed', sep='')
        elif add != None:
            print('Error[1]:', add)
        else:
            print('Error[1]: command was not executed')
        return
    # path error
    elif n == 2:
        if inp != None:
            print('Error[2]: "', inp, '" path does not exist', sep='')
        elif add != None:
            print('Error[2]:', add)
        else:
            print('Error[2]: invalid path')
        return
    # read write error
    elif n == 3:
        if inp != None:
            print('Error[3]: "', inp, '" could not be opened', sep='')
        elif add != None:
            print('Error[3]:', add)
        else:
            print('Error[3]: file could not be read')
        return
    # prototype declaration
    elif n == 4:
        if inp != None:
            pass
        elif add != None:
            pass
        else:
            pass
        return
    else:
        print('Invalid Error code')


# Path functions_________________________

# config path
c_path = 'bin/.configs'


def get_func_list():
    func = os.listdir('bin/')
    for i in range(len(func)):
        func[i] = func[i][:-3]
    rem = ['__init__',
           '__pycach',
           'core',
           'common',
           '.conf',
           '.last_tmp',
           '.except',
           'lock.']
    for i in rem:
        try:
            func.remove(i)
        except ValueError:
            continue
    return sorted(func)


def write_config():
    config = cp.ConfigParser()
    config['prop'] = {'path': 'root/'}
    with open(c_path, 'w') as configs:
        config.write(configs)


def get_path():
    __doc__ = '''
    Gets current path
    of the virtual file
    system.
    returns a string.'''
    config = cp.ConfigParser()
    config.read(c_path)
    path = config['prop']['path']
    return path


def set_path(path):
    __doc__ = '''
    Sets current path
    of the virtual file system.
    returns None'''
    config = cp.ConfigParser()
    config.read(c_path)
    if path[-1] != '/':
        path += '/'
    config.set('prop', 'path', path)
    with open(c_path, 'w') as configs:
        config.write(configs)


def get_last_path(path):
    __doc__ = '''
    Gets the last path in
    the current directory.
    returns path as string'''
    last = str()
    ctr = 0
    i = 1
    if path[-1] != '/':
        path += '/'
    while ctr != 2:
        last += path[-i]
        if path[-i] == '/':
            ctr += 1
        i += 1
    last = last[:-1]
    last = make_s2(list(reversed(last)))
    return last


def get_prv_path():
    __doc__ = '''
    Gets the previous path
    of the current directory.
    returns path as a string.'''
    path = get_path()
    last = get_last_path(path) + '/'
    path = path[:-len(last)]
    return path


def get_prv_path2(path):
    __doc__ = '''
    Gets the previous path
    of the path given as argument.
    returns path as string.'''
    last = get_last_path(path) + '/'
    path = path[:-len(last)]
    return path


# Others_________________________________
def get_args(inp):
    __doc__ = '''
    Gets the arguments seperated
    by a space from a list.
    The argument input cannot have
    spaces in them for now.
    returns arguments as list.'''
    try:
        old = inp[0].replace(' ', '')
        old = inp[0].replace('"', '')
    except IndexError:
        print('1st argument is missing')
        return []
    try:
        new = inp[1].replace(' ', '')
        new = inp[1].replace('"', '')
    except IndexError:
        print('2nd argument is missing')
        return []
    return [old, new]


def isValid(inp):
    __doc__ = '''Checks for valid input'''

    with open('bin/.exception') as exc:
        excepts = exc.readlines()
    for i in excepts:
        # print(r'%s'%i)
        if i[:-1] in inp:
            return True
    return False


def analyze(inp):
    __doc__ = '''
    Basic function to analyze
    the input for other expressions
    returns None'''

    inp = make_s(inp)
    # print(inp)
    # check if is a directory
    if os.path.isdir(get_path() + inp):
        print('"', inp, '" is a directory', sep='')
        return
    elif os.path.isfile(get_path() + inp):
        print('"', inp, '" is a file', sep='')
        return
    # check if is a valid input
    if isValid(inp) or 'inp' in inp:
        err(0, inp)
        return

    try:
        exec('from math import *')
        # math func inp catcher
        # to prevent builtins msg disp
        if inp in dir():
            print('"', inp, '" is a mathematical function', sep='')
            return
        # math func lister__________
        if inp == '--math':
            d = dir()
            d.remove('__doc__')
            d.remove('inp')
            for i in sorted(d):
                print(i)
            return
        e = eval(inp)
        if e != None:
            print(e)
    except SyntaxError:
        print("Couldn\'t evaluate the expression")
    except NameError as e:
        err(0, inp)
    except ZeroDivisionError:
        print('Cannot divide by zero')
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
    except AttributeError as e:
        print(e)
