# pybox
A sandbox version of python

### Disclaimer! 
This is by no means a complete, finished and/or completely safe!
It's a work in progress and you are welcome to use or try to patch it!
Thank you for any help!!!
## Why i chose to do this
Python offers limited sandbox possibilities, with most solutions out there hard to find and often outdated. The idea is to create a sandbox environment in python itself with (best case) no work "outside" of python needed (aka docker or vms for example.)
## Features
- configurable timeouts to prevent infinite loops
- removal of builtins that could cause problems (aka `open(), quit(), exit()`)
- removal of `import` and `__import__`
- ability to pre-import "safe" libraries, such as `math`
## Known bugs
```py
(  
    lambda fc=(lambda n: [c for c in ().__class__.__bases__[0].__subclasses__()  
    if c.__name__ == n][0]): fc("function")(fc("code")(0,0,0,0,0,0,  
    b"KABOOM",(),(),(),"","",0,b"BOOM"),{})()  
)()  
-> main process quit: 
-> Process finished with exit code -1073741819 (0xC0000005)
```
## planned/todo:
- will add later as my time is now limited
- any contributions are welcome and if you do not want to make a pull request at least submit a bug :)
