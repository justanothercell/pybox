# all:
# [__name__, __doc__, __package__, __loader__, __spec__, __build_class__, __import__, abs, all, any, ascii, bin, breakpoint, callable, chr, compile, delattr, dir, divmod, eval, exec, format, getattr, globals, hasattr, hash, hex, id, input, isinstance, issubclass, iter, aiter, len, locals, max, min, next, anext, oct, ord, pow, print, repr, round, setattr, sorted, sum, vars, None, Ellipsis, NotImplemented, False, True, bool, memoryview, bytearray, bytes, classmethod, complex, dict, enumerate, filter, float, frozenset, property, int, list, map, object, range, reversed, set, slice, staticmethod, str, super, tuple, type, zip, __debug__, BaseException, Exception, TypeError, StopAsyncIteration, StopIteration, GeneratorExit, SystemExit, KeyboardInterrupt, ImportError, ModuleNotFoundError, OSError, EnvironmentError, IOError, WindowsError, EOFError, RuntimeError, RecursionError, NotImplementedError, NameError, UnboundLocalError, AttributeError, SyntaxError, IndentationError, TabError, LookupError, IndexError, KeyError, ValueError, UnicodeError, UnicodeEncodeError, UnicodeDecodeError, UnicodeTranslateError, AssertionError, ArithmeticError, FloatingPointError, OverflowError, ZeroDivisionError, SystemError, ReferenceError, MemoryError, BufferError, Warning, UserWarning, EncodingWarning, DeprecationWarning, PendingDeprecationWarning, SyntaxWarning, RuntimeWarning, FutureWarning, ImportWarning, UnicodeWarning, BytesWarning, ResourceWarning, ConnectionError, BlockingIOError, BrokenPipeError, ChildProcessError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError, FileExistsError, FileNotFoundError, IsADirectoryError, NotADirectoryError, InterruptedError, PermissionError, ProcessLookupError, TimeoutError, open, quit, exit, copyright, credits, license, help, _]
# allowed:
# [abs, all, any, ascii, bin, chr, dir, divmod, format, getattr, globals, hasattr, hash,
#                                 hex, id, isinstance, issubclass, iter, aiter, len, locals, max, min, next, anext, oct,
#                                 ord, pow, print, repr, round, setattr, sorted, sum, vars, None, Ellipsis, NotImplemented,
#                                 False, True, bool, bytearray, bytes, classmethod, complex, dict, enumerate, filter, float,
#                                 frozenset, property, int, list, map, object, range, reversed, set, slice, staticmethod,
#                                 str, super, tuple, type, zip,
#                                 # errors
#                                 BaseException, Exception, TypeError, StopAsyncIteration,
#                                 StopIteration, GeneratorExit, SystemExit, KeyboardInterrupt, ImportError,
#                                 ModuleNotFoundError, OSError, EnvironmentError, IOError, WindowsError, EOFError,
#                                 RuntimeError, RecursionError, NotImplementedError, NameError, UnboundLocalError,
#                                 AttributeError, SyntaxError, IndentationError, TabError, LookupError, IndexError,
#                                 KeyError, ValueError, UnicodeError, UnicodeEncodeError, UnicodeDecodeError,
#                                 UnicodeTranslateError, AssertionError, ArithmeticError, FloatingPointError,
#                                 OverflowError, ZeroDivisionError, SystemError, ReferenceError, MemoryError, BufferError,
#                                 Warning, UserWarning, EncodingWarning, DeprecationWarning, PendingDeprecationWarning,
#                                 SyntaxWarning, RuntimeWarning, FutureWarning, ImportWarning, UnicodeWarning,
#                                 BytesWarning, ResourceWarning, ConnectionError, BlockingIOError, BrokenPipeError,
#                                 ChildProcessError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError,
#                                 FileExistsError, FileNotFoundError, IsADirectoryError, NotADirectoryError,
#                                 InterruptedError, PermissionError, ProcessLookupError, TimeoutError]
# parse to key-value str:
# b = allowed_builtins
# str_b = [str(p) if not hasattr(p, '__name__') else p.__name__ for p in b]
# ', '.join("'"+str_p+"': "+str_p for str_p in str_b

safe_builtin_names = ['abs', 'all', 'any', 'ascii', 'bin', 'chr', 'dir', 'divmod', 'format', 'getattr', 'globals', 'help',
                      'hasattr', 'hash', 'hex', 'id', 'isinstance', 'issubclass', 'iter', 'aiter', 'len', 'locals', 'max', 
                      'min', 'next', 'anext', 'oct', 'ord', 'pow', 'print', 'repr', 'round', 'setattr', 'sorted', 'sum', 
                      'vars', 'None', 'Ellipsis', 'NotImplemented', 'False', 'True', 'bool', 'bytearray', 'bytes', 
                      'classmethod', 'complex', 'dict', 'enumerate', 'filter', 'float', 'frozenset', 'property', 'int', 
                      'list', 'map', 'object', 'range', 'reversed', 'set', 'slice', 'staticmethod', 'str', 'super', 'tuple',
                      'type', 'zip', 'BaseException', 'Exception', 'TypeError', 'StopAsyncIteration', 'StopIteration', 
                      'GeneratorExit', 'SystemExit', 'KeyboardInterrupt', 'ImportError', 'ModuleNotFoundError', 'EOFError', 
                      'RuntimeError', 'RecursionError', 'NotImplementedError', 'NameError', 'UnboundLocalError',
                      'AttributeError', 'SyntaxError', 'IndentationError', 'TabError', 'LookupError', 'IndexError',
                      'KeyError', 'ValueError', 'UnicodeError', 'UnicodeEncodeError', 'UnicodeDecodeError',
                      'UnicodeTranslateError', 'AssertionError', 'ArithmeticError', 'FloatingPointError', 'OverflowError',
                      'ZeroDivisionError', 'SystemError', 'ReferenceError', 'MemoryError', 'BufferError', 'Warning',
                      'UserWarning', 'EncodingWarning', 'DeprecationWarning', 'PendingDeprecationWarning', 'SyntaxWarning',
                      'RuntimeWarning', 'FutureWarning', 'ImportWarning', 'UnicodeWarning', 'BytesWarning', 'ResourceWarning',
                      'ConnectionError', 'BlockingIOError', 'BrokenPipeError', 'ChildProcessError', 'ConnectionAbortedError',
                      'ConnectionRefusedError', 'ConnectionResetError', 'FileExistsError', 'FileNotFoundError',
                      'IsADirectoryError', 'NotADirectoryError', 'InterruptedError', 'PermissionError', 'ProcessLookupError',
                      'TimeoutError']

class MISSING: pass

safe_builtins = {}
for name in safe_builtin_names:
    if __builtins__.get(name, MISSING) is not MISSING:
        safe_builtins[name] = __builtins__[name]

safe_libraries = ['math']


def generate_pyfuncs():
    return {'py': lambda *args, **kwargs: ..., 'python': lambda *args, **kwargs: ...}
