from pybox import PyBox

box = PyBox()


# print result is called AFTER the code has run!
def print_result(message):
    print('from box:\n', message, sep='')

# only setting 'printer' will automatically redirect error messages to it,
# so if its the same functioin, dont bother to do it twice :)
box.set_printer(printer=lambda message: print_result(message), err_printer=lambda message: print_result(message))
box.exec("""
print('hello world')
def func():
    print(33)
    print(1)
    return True
print(func())
""", abort_time=1, callback=lambda r, t: print('return value, time:', r, t))
# note that callback is supposed to do actually useful stuff
print('end')

# read out variables/functions:
# attention! this is most likely not safe(yet)! 
# executes the func function we created earlier
print(box.variables["func"]())

