# https://realpython.com/python-print/
import os

##################################################
# INTRODUCTION
##################################################
print()
print("INTRODUCTION")
# an empty print statement is the same as '\n'

print()
print('hello') # just an example string
print()

# passing a string directly to print
print('Please wait while the program is loading...')

# String literals promote code reuse
message = ("Please wait while the program is loading...")
print(message)

# There is also string concatenation
print('Hello, ' + os.getlogin() + '! How are you?')

# There are fstrings which were introduced in python 3.6 
# which will be worth another look at some point
# as these offer the most efficient syntax of all

print(f'Hello, {os.getlogin()}! How are you!')

# To concatenate numbers to strings you must use the str() method
print('My age is ' + str(42))

print(42)                              # int 
print(3.14)                            # float
print(1 + 2j)                          # complex
print(True)                            # bool
print([1, 2, 3])                       # list
print((1, 2, 3))                       # tuple
print({'red', 'green', 'blue'})        # set
print({'name': 'Alice', 'age': 42})    # dictionary
print('hello')                         # string 
print(None)                            # None

# print implicitly calls the str() method

##################################################
# SEPARATING MULTIPLE ARGUMENTS
##################################################
print()
print("SEPARATING MULTIPLE ARGUMENTS")
# Print can is of the print(*args) so it can take any number of arguments
print('My name is', os.getlogin(), 'and I am', 42)

# There are four keyword arguments associated with the print() function

##################################################
# sep KEYWORD ARGUMENT
##################################################
print('hello', 'world', sep=None) # This doesn't remove the separtor
print('hello', 'world', sep=' ')
print('hello world')

# In order to remove the separator then sep must equal an empty string
print('hello', 'world',sep='')

# You can join arguments using separte lines if you want 
print('hello', 'world',sep='\n')

# A more useful example of the sep parameter would be creating file paths
print('home', 'usr', 'Documents', sep='/')
# more accurately would be either of the 2 following print statements
print('/home', 'usr', 'Documents', sep='/')
print('','home', 'usr', 'Documnets', sep='/')

# Joining elements of a list with different types requires the * operator
print(*['jdoe is', 42, 'years old'])

# you could also export data to comma separated value format
print(1, 'Python tricks', 'Dan Bader', sep=',')

# You join elements of with elements that are multiple characters
print('node', 'child', 'child', sep=' -> ')

# There are four keyword arguments associated with the print() function
print('hello', 'world', sep=None) # This doesn't remove the separtor
print('hello', 'world', sep=' ')
print('hello world')

# In order to remove the seporator then sep must equal an empty string
print('hello', 'world',sep='')

# You can join arguments using separte lines if you want 
print('hello', 'world',sep='\n')

# A more useful example of the sep parameter would be creating file paths
print('home', 'usr', 'Documents', sep='/')
# more accurately would be either of the 2 following print statements
print('/home', 'usr', 'Documents', sep='/')
print('','home', 'usr', 'Documnets', sep='/')

# Joining elements of a list with different types requires the * operator
print(*['jdoe is', 42, 'years old'])

# you could also export data to comma separated value format
print(1, 'Python tricks', 'Dan Bader', sep=',')

# You join elements of with elements that are multiple characters
print('node', 'child', 'child', sep=' -> ')

##################################################
# end KEYWORD ARGUMENT
##################################################

# Can be used to disable the default '\n' string at the end of every print
# statement.
print("Checking file integrity...", end='')
print("ok")

# These three functions will print each sentence one after the other on one line 
print("The first sentence", end=".")
print("The second sentence", end=".")
print("The last sentence", end=".")


##################################################
# sep & end KEYWORD ARGUMENTS COMBINED
##################################################

print('Mercury', 'Venus', 'Earth', sep=', ', end=', ')
print('Mars', 'Jupiter', 'Saturn', sep=', ', end=', ')
print('Uranus', 'Neptune', 'Pluto', sep=', ')

# You can pad the print the function as well
print()
print('Printing in a nutshell', end='\n * ')
print('Calling Print', end='\n * ')
print('Separating line breaks', end='\n * ')
print('Preventing line breaks')
print()

# The problem with the following is the new lines are preserved from the 
# which makes everything print with an extra line between which is problematic
with open('file.txt') as file_object:
    for line in file_object:
        print(line)
print()
with open('file.txt') as file_object:
    for line in file_object:
        print(line.strip())

print()
# Alternatively...
print('Alternatively...')
with open('file.txt') as file_object:
    for line in file_object:
        print(line, end='')
print()
##################################################
# PRINTING TO A FILE: encoding and file
##################################################
import sys

# You can access all streams in python through the sys module
print(sys.stdin)
print(sys.stdin.fileno())
print(sys.stdout)
print(sys.stdout.fileno())
print(sys.stderr)
print(sys.stderr)

# This will make your code stream redirection at the operating system level
# which may or may not be the desired behaviour
with open('file1.txt', mode='w') as file_object:
    print('hello world', file = file_object)

# CAUTION: DON'T USE PRINT() FOR TRYING TO WRITE BINARY DATA

print()

#print("BINARY DATA WRITING")
#with open('binary.txt', 'wb') as file_object:
#    file_object.write(bytes(4))
#    file_object.write(b'\xff')

# sys.stdout is a character stream.
# in order to write stdout byte stream you have to dig a little deeper to
# get to it
num_bytes_written = sys.stdout.buffer.write(b'\x41\x0a') 
# this prints A and a newline charcter using hexadicimal. 41 = 65, 0a = 10

# the stream will do the default encoding for you, which is usually UTF-8

# instead of using a real file to do this we can creat a fake one
import io
fake_file = io.StringIO()
print('hello world', file=fake_file)
fake_file.getvalue()

##################################################
# BUFFERING PRINT() CALLS: flush keyword
##################################################

# In the last section you learnt that print() delegates printing to a file like
# object like sys.stdout

print()
# A PRIMITIVE COUNT DOWN TIMER

#import time
#
#num_seconds = 3 
#for countdown in reversed(range(num_seconds + 1)):
#    if countdown > 0:
#        #print(countdown, end='...')
#        print(countdown, end='...', flush=True)
#        time.sleep(1)
#    else:
#        print('Go!')

print("There are three kinds of buffers", end="\n * ")
print("Unbuffered", end="\n * ")
print("Line-buffered", end="\n * ")
print("Block-buffered") 
print()
# Unbuffered means that all writes to standard out have an immediate effect
# Line buffered waits until a line break appears somewhere in the buffer 
# before firing
# block buffering allows filling up to a certain limit before being released

# Buffering reduces the number of expensive input and output calls

##################################################
# CUSTOM DATA TYPES
##################################################

from collections import namedtuple

Person = namedtuple("Person", "name age") 
jdoe = Person('John Doe', 42)
print(jdoe)

# this is a very lazy but quick way of making essentially a class

class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age
 
print("Traditional Class creation")
jdoe = Person('John Doe', 42)
print(jdoe)
print()
print("""Here we get a strange output which is the default representation of 
objects.""")
# A nice trick could be to create a combined class that is a named tuple with 
# two attributes that you can customise

class Person(namedtuple('Person', 'name age')):
    pass

# In python 3 an elipses (...) can be used as a place holder for pass so that 
# we avoid an indentation error by accident

# The problem with this namedtuple class combination is that because tuples are 
# immutable this makes the Person datatype immutable

# To get past this problem python 3.7 introduced data classes which you can 
# think of as mutable tuples

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

    def celebrate_birthday(self):
        self.age += 1

print()
print("Using dataclass object from dataclasses library we get what we want.") 
jdoe = Person('John Doe', 42)
jdoe.celebrate_birthday()
print(jdoe)

##################################################
# str(), rpr(), eval() 
##################################################

# The str() method looks for one of 2 magic methods within the class body.
# 1. def __str__(self): used for returning short text of key attributes
# 2. def __repr__(self): used for returning the complete info of an object so 
#                           so that it's state can be restored from a string
print()
print(repr(jdoe))
print(type(eval(repr(jdoe))))

# Below is an example of where both magic methods are implemented in a class

class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def __str__(self):
        return self.login   # This information isn't sensative

    def __repr__(self):
        return f"User('{self.login}', '{self.password}')"

print()
user = User('jdoe', 's3cret')
print(user)
print("If you put the instance in a square brace you get the full info.")
print([user])
print("""This is because sequences such as lists and tuples, implement their
.__str__() method so that all of their elements are first converted with
__repr__""")


