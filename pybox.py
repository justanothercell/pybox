import sys
import time
import traceback
from thread2 import Thread
from copy import deepcopy
from io import StringIO
from contextlib import redirect_stdout
from typing import Callable, Any

from pybox_util import safe_builtins, safe_libraries, generate_pyfuncs


class PyBox:
    def __init__(self, custom_builtins: dict[str, Any] = safe_builtins, libraries: list[str] = safe_libraries):
        self.variables = {'__builtins__': deepcopy(custom_builtins),
                          **{str(lib): __import__(lib) for lib in libraries},
                          **generate_pyfuncs()}
        self.printer = print
        self.err_printer = None
        self.total_time = 0

    # for arg/kwarg printer:
    # lambda *args, **kwargs: print('from box:', *args, **kwargs)
    def set_printer(self, printer: Callable, err_printer: Callable = None):
        self.printer = printer
        self.err_printer = err_printer

    def exec(self, code: str, abort_time=0, callback=lambda ret_val, exec_time: ..., halt_main_thread=False):
        start_time = time.perf_counter_ns()

        def _exec():
            ret_val = 0
            f = StringIO()
            try:
                with redirect_stdout(f):
                    exec(code, self.variables)
                s = f.getvalue()
                self.printer(s)
            except BaseException:
                s = f.getvalue()
                self.printer(s)
                exc_type, exc_value, exc_traceback = sys.exc_info()
                if not isinstance(exc_value, SystemExit):
                    ret_val = 1
                    exception_array = traceback.format_exc()
                    i = tuple(
                        1 if 'File "<string>", line' in line else 0 for line in exception_array.splitlines()).index(1)
                    exception_str = '\n'.join([line.strip() for line in exception_array.splitlines()[i:]])
                    if self.err_printer is not None:
                        self.err_printer(exception_str)
                    else:
                        self.printer(exception_str)

            exec_time = (time.perf_counter_ns() - start_time) / 1e9
            self.total_time += exec_time
            callback(ret_val, exec_time)

        thread = Thread(target=_exec)
        thread.start()
        if abort_time != 0:
            def _abort():
                time.sleep(abort_time)
                if thread.is_alive():
                    exec_time = (time.perf_counter_ns() - start_time) / 1e9
                    thread.terminate()
                    self.total_time += exec_time
                    callback(2, exec_time)

            abort_thread = Thread(target=_abort)
            abort_thread.start()
        if halt_main_thread:
            thread.join()
