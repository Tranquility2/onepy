import os
if os.name == 'nt':
    from pyreadline import Readline
    readline = Readline()
else:
    import readline # optional, will allow Up/Down/History in the console
import code

variables = globals().copy()
variables.update(locals())
shell = code.InteractiveConsole(variables)
shell.interact()
