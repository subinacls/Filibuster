# encoding: utf-8
#!/usr/bin/env python
'''
used for error reporting on modules which crash for easy diagnostics and location of problematic module
'''

import inspect

class modreporter:

    def __init__(self):
        pass

    def mod_inspect(self):
        frm = inspect.trace()[-1]
        mod = inspect.getmodule(frm[0])
        modname = mod.__name__ if mod else frm[1]
        return modname




