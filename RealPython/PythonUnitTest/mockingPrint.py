# https://realpython.com/python-print/#understanding-python-print

# You can test behaviours by mocking real objects or functions
# In this example we are going to mock the print function to test BEHAVIOUR

# The typical method in statically typed languages is to make use of dependency
# injection. The problem with this is it means sometimes you have to change the 
# code in question. This isn't always possible if it is defined in an external 
# library.

##################################################
# DEPENDENCY INJECTION EXAMPLE
##################################################

def download(url, log=print):
    log(f'Downloading {url})') 
    # ... 

# Notice how log is a keyword argument which is assigned to the print() function
# This means that when the download function is called by default, the print 
# function will be called.
# However if we create a mock_print function to test behaviour then we can 

#def mock_print(message):
#    mock_print.last_message = message
#
#download('resource', mock_print)
#assert 'Downloading resource' == mock_print.last_message

def mock_print(message):
    mock_print.last_message = message

download('resource', mock_print)
# assert 'Downloading resource)' == mock_print.last_message

# for some reason assert isn't working despite what Real Python says...

