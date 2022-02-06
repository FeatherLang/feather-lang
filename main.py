#!/usr/bin/env python

import os
import webbrowser
from modules.error import Error

fileDir = input("File Directory: ")

poopcode = open(fileDir, "r")
if poopcode.name.endswith(".pc") or poopcode.name.endswith(".poopcode") or poopcode.name.endswith(".poop"):
    pass
else:
    Error("File is not PoopCode")


file_raw = poopcode.read()
file = file_raw.splitlines()
poopcode.close()
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
        #os.system(poopcode"ping(\"{ping_arg}\")")
        response = os.system("ping " + ping_arg)
    elif line.startswith("RELAY "):
        #remove the "HACK"
        relay_arg = line[6:]
        if relay_arg == "" or relay_arg == None:
            Error(a = "SYNTAX ERR:", b = "argument not found.")
        print(relay_arg)
    elif line.startswith("WEBSITE "):
        #remove the "HACK"
        website = line[8:]
        if not website.endswith("https://"):
            website = "https://" + website
        webbrowser.open(website)
    elif line.startswith("CALC "):
        #remove the "HACK"
        calc = line[5:]
        print(calc + " = " + str(eval(calc)))
    elif line == "QUIT" or line == "EXIT":
        quit(0)
    else:
        Error(a = "SYNTAX ERR:", b = f"function \"{line.split()[0]}\" not found.")