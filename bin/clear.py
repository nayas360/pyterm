# clear screen command
from os import system
from platform import system as sysname


def _help():
    usage = '''
Usage: clear'''
    print(usage)


def main():
    system_name = sysname()
    if system_name == 'Windows':
        system('cls')
    elif system_name == 'Linux':
        system('clear')
    return
