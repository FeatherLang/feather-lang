from modules.colors import *

def Error(b, a = "ERR:"):
    print(colors.red + f"{a} " + colors.reset + b)
    exit(0)