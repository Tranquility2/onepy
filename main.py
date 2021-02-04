import readline # optional, will allow Up/Down/History in the console
import code
variables = globals().copy()
variables.update(locals())
shell = code.InteractiveConsole(variables)
shell.interact()

