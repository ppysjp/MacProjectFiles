# https://realpython.com/python-print/#understanding-python-print

##################################################
# UNDERSTANDING PYTHON PRINT
##################################################
print("UNDERSTANDING PYTHON PRINT")
print()
print("""After reading this you will be more conscious of what the print 
function is for, to use it more efficently and how printing has improved over
the years in python!""")
print()
print(print)

##################################################
# You can redefine print if you want

#import builtins
#println = builtins.print
#def print(*args, **kwargs):
#    builtins.print(*args, **kwargs, end='')

# println('hello')
# print('hello\n')

##################################################

# It is none mathematical function in a sense as it returns only None as a value

value = print('hello world')
print(value)


##################################################
# Dependency Injection
##################################################

def download(url, log=print):
    log(f'Downloading {url}')
    # ...

def custom_print(*args):  
    pass

download('/js/app.js', log=custom_print)

# Here the print function is completely disabled by substituting in a callable
# (in this case custom_print) which does nothing. Being able todo this is 
# useful for testing and things.

#########################################################################
# Composition: allows you to combine a few functions a new same kind one
#########################################################################
from functools import partial
import sys
redirect = lambda function, stream: partial(function, file=stream)
prefix = lambda function, prefix: partial(function, prefix)
error = prefix(redirect(print, sys.stderr), '[ERROR]')
error('Something went wrong')

# This is an example of functional programming, a paradigm to come back to
print()
user = 'jdoe'
print('Hi') if user is None else print(f'Hi, {user}.')

# Print was a statement in python 2 which used to cause a lot of headaches
# This basically meant you could not mock the print statement in python 2 

# Python 3 can leverage sequence unpacking which is much nicer

values = ['jdoe', 'is', 42, 'years old']
print(*values)
