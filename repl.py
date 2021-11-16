from typing import Any, Callable

from camcam.pybox.pybox import PyBox


def is_indentation_error(code: str) -> bool:
    try:
        compile(code, '<string>', 'exec')
    except IndentationError:
        return True
    except SyntaxError:
        return False
    else:
        return False


def get_input(prompt='!>> ') -> str:
    first_line = input(prompt)
    if is_indentation_error(first_line):
        code = [first_line]
        while True:
            try:
                line = input('... ')
            except EOFError:
                break
            if line == '':
                break
            code.append(line)
        code = '\n'.join(code)
    else:
        code = first_line
    return code


def repl(box: PyBox = None, abort_time: int = 0, prompt='!>> ',
         exec_info_printer: Callable = print, echo_input: Callable = None) -> None:
    if exec_info_printer is None:
        exec_info_printer = lambda x: ...
    if echo_input is None:
        echo_input = lambda x: ...
    if box is None:
        box = PyBox()
    elif not isinstance(box, PyBox):
        raise TypeError(f'box arg must be of type PyBox not {box.__class__!r}')

    def next_repl(ret_val: int, exc_time: float) -> None:
        if ret_val == 2:
            exec_info_printer('aborted')
        else:
            exec_info_printer(f'executed in {exc_time * 1e6:.5f}μs')
        try:
            _repl()
        except EOFError:
            exec_info_printer('Bye!')

    def _repl() -> None:
        code = get_input(prompt=prompt)
        echo_input(prompt + code)
        while code == '':
            code = get_input()

        box.exec(code, callback=next_repl, abort_time=abort_time)

    try:
        _repl()
    except EOFError:
        exec_info_printer('Bye!')
