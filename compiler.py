import os
from datetime import date, datetime
from modules.error import Error
fileDir = input("File Directory: ")

poopcode = open(fileDir, "r")
if poopcode.name.endswith(".pc") or poopcode.name.endswith(".poopcode"):
    pass
else:
    Error("File is not PoopCode")


file_raw = poopcode.read()
file = file_raw.splitlines()

if not os.path.exists("build"):
    os.mkdir("build")
    if os.path.exists("build/output.py"):
        os.remove("build/output.py")

python_code = open('build/output.py', 'w')
print("Compiling PoopCode --> Python")
python_code.write(f"# Compiled from PoopCode at {datetime.now().strftime('%B %d, %Y at %H:%M')}. \nimport os\n\n")


for line in file:
    if line.startswith("HACK ") or line.startswith("DDOS " ):
        #remove the protocol
        ping = line[5:]

        if ping.startswith("https://"):
            ping = ping[8:]
        elif ping.startswith("http://"):
            ping = ping[7:]

        python_code.write(f'os.system("ping {ping}")\n')
    elif line.startswith("RELAY "):
        relay = line[6:]
        python_code.write(f'print("{relay}")\n')
    elif line == "QUIT":
        python_code.write(f'quit(0)\n')
        

python_code.close()
poopcode.close()
print("Compiled PoopCode. Navigate to ./build/output.py")