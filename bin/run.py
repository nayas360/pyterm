# run function
from importlib import import_module as _import

from lib.utils import *


def _help():
    usage = '''
Usage: run (file)

Where (file) is a valid
script file

-h            Print this help
'''
    print(usage)


def main(argv):
    if len(argv) < 1 or '-h' in argv:
        _help()
        return
    # The shell doesnt send the
    # command name in the arg list
    # so the next line is not needed
    # anymore
    # argv.pop(0) #remove the command
    # get the path to the file
    inp = make_s(argv)
    path = get_path() + inp

    # check if it is a file
    if inp in os.listdir(get_path()) and not os.path.isfile(path):
        err(3, add=inp + ' is a directory')
        return
    if inp not in os.listdir(get_path()):
        err(2, path)
        return

    # if is file read data
    with open(path) as f:
        data = f.readlines()
    # Now try executing each line
    for i in data:
        i = i.split()
        f_list = get_func_list()
        try:
            f = i[0]
        except IndexError:
            continue
        if f in f_list:
            i.pop(0)
            mod = 'bin.' + f
            m = _import(mod)
            try:
                m.main(i)
            except TypeError:
                m.main()
            except AttributeError:
                err(1, f)
        elif f not in f_list:
            i = make_s(i)
            try:
                e = eval(i)
                if e != None:
                    print(e)
            except SyntaxError:
                try:
                    exec(i)
                except SyntaxError as e:
                    print(e)
                    return
            except NameError as e:
                err(0, i)
            except ZeroDivisionError:
                print('Cannot divide by zero')
            except TypeError as e:
                print(e)
            except ValueError as e:
                print(e)
            except AttributeError as e:
                print(e)
