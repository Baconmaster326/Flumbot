import time
import os
import psutil

plist = []

PROCNAME = "python.exe"

for each in psutil.pids():
    each = psutil.Process(each)
    try:
        print(each.name)
        if "python.exe" in str(each.name):
            plist.append(each)
    except:
        continue
print(plist)

if plist[0].create_time() < plist[1].create_time():
    plist[0].kill()
else:
    plist[1].kill()
        
print("waiting")
time.sleep(120)
os.startfile('FlumbotGOTEdition.py')
exit()
