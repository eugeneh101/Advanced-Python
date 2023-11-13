import pdb

def flawed_function():
    x = 1
    y = 0
    pdb.set_trace()
    return x / y

flawed_function()
