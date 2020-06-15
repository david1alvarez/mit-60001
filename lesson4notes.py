''' Decomposition, Abstraction, and Functions
    Abstraction - You dont need to know how it works in order to use it.
    Decomposition - Break out functional components of your code
        How you organize your code
'''

# docstrings let you describe your function for future reference
def example_func():
    """this is just an example function.
        If its more complicated, we might need to write more lines.
        Linebreaks are interpreted as spaces"""
    return

''' When you call a function, the program spins up a new environment to
    run the function definition in. Python treats all variables that are
    defined in the function to be local variables, but variables that exist
    globally can still be called from within the function. If a variable is
    defined globally but not locally, calling it locally will call the 
    global variable. Initializing a new variable with the same name as a 
    global variable will not overwrite the global variable, it will instead
    create a new local variable. To modify a global variable from within a 
    function, you need to use the global keyword
'''

x = 4
print(x)
def access_global():
    '''sets the global variable x to 5'''
    global x # generally frowned upon
    x = 5
    return None # this gets added automatically, not needed to be added

access_global()
print(x)

''' When calling a "global" variable, python looks in the 
    scope that called the function to see if the variable exists.
    This is a potential bug-causing issue as the scope referred to is
    not always the global scope, but might be the scope of another function
    where that function is the one that called the current function.
'''

# http://pythontutor.com python tutor is an easy way to visualize whats going on in a program