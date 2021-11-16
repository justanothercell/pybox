from repl import repl
from pybox import PyBox

box = PyBox()

repl(box)

# !>> def k(x):
# ... 	print(x)
# ... 	print(y)
# ...
# executed in 1566.30000μs
# !>> k(1)
# 1
#
# File "<string>", line 1, in <module>
# File "<string>", line 3, in k
# NameError: name 'y' is not defined
# executed in 1607.80000μs
# !>> print([x*x for x in range(10)])
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#
# executed in 927.40000μs
# !>>
