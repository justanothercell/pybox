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

safe_builtins = {
    'abs': abs, 'all': all, 'any': any, 'ascii': ascii, 'bin': bin, 'chr': chr, 'dir': dir,
    'divmod': divmod, 'format': format, 'getattr': getattr, 'globals': globals, 'help': help,
    'hasattr': hasattr, 'hash': hash, 'hex': hex, 'id': id, 'isinstance': isinstance,
    'issubclass': issubclass, 'iter': iter, 'aiter': aiter, 'len': len, 'locals': locals,
    'max': max, 'min': min, 'next': next, 'anext': anext, 'oct': oct, 'ord': ord,
    'pow': pow, 'print': print, 'repr': repr, 'round': round, 'setattr': setattr,
    'sorted': sorted, 'sum': sum, 'vars': vars, 'None': None, 'Ellipsis': Ellipsis,
    'NotImplemented': NotImplemented, 'False': False, 'True': True, 'bool': bool,
    'bytearray': bytearray, 'bytes': bytes, 'classmethod': classmethod,'complex': complex,
    'dict': dict, 'enumerate': enumerate, 'filter': filter, 'float': float,
    'frozenset': frozenset, 'property': property, 'int': int, 'list': list, 'map': map,
    'object': object, 'range': range, 'reversed': reversed, 'set': set, 'slice': slice,
    'staticmethod': staticmethod, 'str': str, 'super': super, 'tuple': tuple, 'type': type,
    'zip': zip,
    'BaseException': BaseException, 'Exception': Exception, 'TypeError': TypeError,
    'StopAsyncIteration': StopAsyncIteration, 'StopIteration': StopIteration,
    'GeneratorExit': GeneratorExit, 'SystemExit': SystemExit,
    'KeyboardInterrupt': KeyboardInterrupt, 'ImportError': ImportError,
    'ModuleNotFoundError': ModuleNotFoundError, 'EOFError': EOFError,
    'RuntimeError': RuntimeError, 'RecursionError': RecursionError,
    'NotImplementedError': NotImplementedError, 'NameError': NameError,
    'UnboundLocalError': UnboundLocalError, 'AttributeError': AttributeError,
    'SyntaxError': SyntaxError, 'IndentationError': IndentationError,
    'TabError': TabError, 'LookupError': LookupError, 'IndexError': IndexError,
    'KeyError': KeyError, 'ValueError': ValueError, 'UnicodeError': UnicodeError,
    'UnicodeEncodeError': UnicodeEncodeError, 'UnicodeDecodeError': UnicodeDecodeError,
    'UnicodeTranslateError': UnicodeTranslateError, 'AssertionError': AssertionError,
    'ArithmeticError': ArithmeticError, 'FloatingPointError': FloatingPointError,
    'OverflowError': OverflowError, 'ZeroDivisionError': ZeroDivisionError,
    'SystemError': SystemError, 'ReferenceError': ReferenceError,
    'MemoryError': MemoryError, 'BufferError': BufferError, 'Warning': Warning,
    'UserWarning': UserWarning, 'EncodingWarning': EncodingWarning,
    'DeprecationWarning': DeprecationWarning,
    'PendingDeprecationWarning': PendingDeprecationWarning, 'SyntaxWarning': SyntaxWarning,
    'RuntimeWarning': RuntimeWarning, 'FutureWarning': FutureWarning,
    'ImportWarning': ImportWarning, 'UnicodeWarning': UnicodeWarning,
    'BytesWarning': BytesWarning, 'ResourceWarning': ResourceWarning,
    'ConnectionError': ConnectionError, 'BlockingIOError': BlockingIOError,
    'BrokenPipeError': BrokenPipeError, 'ChildProcessError': ChildProcessError,
    'ConnectionAbortedError': ConnectionAbortedError,
    'ConnectionRefusedError': ConnectionRefusedError,
    'ConnectionResetError': ConnectionResetError, 'FileExistsError': FileExistsError,
    'FileNotFoundError': FileNotFoundError, 'IsADirectoryError': IsADirectoryError,
    'NotADirectoryError': NotADirectoryError, 'InterruptedError': InterruptedError,
    'PermissionError': PermissionError, 'ProcessLookupError': ProcessLookupError,
    'TimeoutError': TimeoutError
}

safe_libraries = ['math']


def generate_pyfuncs():
    return {'py': lambda *args, **kwargs: ..., 'python': lambda *args, **kwargs: ...}