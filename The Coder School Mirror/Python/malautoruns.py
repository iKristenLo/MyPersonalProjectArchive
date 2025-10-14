import platform
import subprocess

archi = platform.architecture()
autorun = ""
machine = platform.machine()
if archi[1] != 'WindowsPE':
    print("This Script Can Only Be Ran On Windows Systems!")
    exit(1)

if archi[0] == '64bit' and machine == "ARM64":
    autorun = "autorunsc64a.exe"
elif archi[0] == '32bit':
    autorun = "autorunsc.exe"
elif archi[0] == '64bit':
    autorun = "autorunsc64.exe"
else:
    print("Unable to determine system architecture!")
    exit(2)

subprocess.run([autorun,"-accepteula","-vt","-vrs","-h","-ct","-a *","-o autoruns-vt.csv"])
