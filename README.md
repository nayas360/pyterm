# pyterm
A terminal emulator complete with a shell enriched with commands and its own file system written in pure python

This is an old project of mine from 2014

The aim of this project is to emulate a shell environment written in pure python

As you may have noticed the version number starts from 1.6 as versions prior to that were simply not working when I
decided to upload all the code to GitHub.

# Instructions for creating your own commands

* If you want to create a command say _`foo`_, you have to add a file called _`foo.py`_ in the bin folder.
 
* This _`foo.py`_ file has to have a function called _`main`_. This function should be the entry point for your command. The shell calls this function to run your module. The shell will raise an error if it cannot call the main function.
 
* If you use a library in your code that is not included in the standard python library you can put it in the libs folder and import it as _`lib.LIB_NAME`_ in your file.
 
* You can choose to receive arguments from the shell in a single variable. The arguments are sent as a list of strings, you need to process them accordingly as required. **NOTE** that the name of the command is **NOT** the first argument in the list, as it is generally in standard implementations. It was there in some of the previous versions though, but it is quite unnecessary and was dropped in the more recent versions.
 
That's all you need to know to write you own commands !!
 
Also there are some utility functions which I created in the _`lib.utils`_ file. See some of the provided commands as to how to use them. check out lib.utils file to see what the functions do. They might look complicated ;)