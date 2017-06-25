# Help function

u = '''
[help]
=> To list available commands 
   use "lcom" command

=> For extra info and help on
   particular commands pass
   "-h" as argument with the
   required command.If help is
   available, it will be shown.

=> Enter mathematical
   expressions directly into the
   shell to evaluate them. Also
   you can issue a special keyword
   "--math" to list the supported 
   mathematical functions.

=> Issue "exit" to exit the shell
'''

v = '''
[version]
v2.3a

[author]
Sayan Dutta
'''

i = '''
[info]
This program is a shell/terminal
environment simulator with a fairly
easy to understand API for extending
the program and/or the commands that
the shell can recognize.

see docs for more details.
'''

h = '''Usage: help [options]

[options]:

-help         Print help
-i            Print info
-v            Print version
-h            Print this msg
'''

def main(argv):
    # help gets an empty argv,
    # shell doesnt send the
    # comm name anymore
    if '-h' in argv:
        print(h)
        return
    if '-v' in argv:
        print(v)
        return
    if '-i' in argv:
        print(i)
        return
    if '-help' in argv:
        print(u)
        return
    print(i, u,v)
