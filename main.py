#!/usr/bin/env python

import os
from modules.error import Error

fileDir = input("File Directory: ")

f = open(fileDir, "r")
if f.name.endswith(".pc") or f.name.endswith(".poopcode"):
    pass
else:
    Error("File is not PoopCode")


file_raw = f.read()
file = file_raw.splitlines()
f.close()
for line in file:
    if(line == ""):
        pass
    if line.startswith("HACK ") or line.startswith("DDOS " ):
        #remove the "HACK"
        ping_arg = line[5:]
        if(ping_arg == "" or ping_arg == None):
            Error(b = "Argument not satisfied", a = "SYNTAX ERR:")

        #remove the protocol
        if ping_arg.startswith("https://"):
            ping_arg = ping_arg[8:]
        elif ping_arg.startswith("http://"):
            ping_arg = ping_arg[7:]

        #run the ping command
        #os.system(f"ping(\"{ping_arg}\")")
        response = os.system("ping " + ping_arg)
    elif line.startswith("RELAY "):
        #remove the "HACK"
        relay_arg = line[6:]
        if relay_arg != "" or relay_arg != None:
            Error(a = "SYNTAX ERR:", b = "argument not found.")
        print(relay_arg);
    elif line == "QUIT":
        quit_arg = line[5:]
        quit(quit_arg)
    else:
        Error(a = "SYNTAX ERR:", b = f"function \"{line.split()[0]}\" not found.")