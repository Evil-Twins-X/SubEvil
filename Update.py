import requests
import os
import sys
from Lib.Brand import *
from  colored import fg,attr
import time
def system():
    os.system('cls' if os.name == 'nt' else 'clear')
def update(version=sys.argv[1]):
    CheckUpdate = "https://raw.githubusercontent.com/Evil-Twins-X/MyToolsUpdate/main/SubEvil.txt"
    req = requests.get(url=CheckUpdate).text
    if version in req :
        print(f"{fg(40)}✅💯 The tool is updated ✅💯{attr(0)}")
    else: 
        for i in req.splitlines():
            if "/" in i:
                print(f"{fg(40)} This file needs updating [{i}] {attr(0)}")
                urlGetupdate = f"https://raw.githubusercontent.com/Evil-Twins-X/SubEvil/main/{file}"
                os.remove("{i}")
                textfile =requests.get(urlGetupdate).text
                open(f"{i}").write(textfile)

system()
print(Brand())
print("Wite Check For Update ")
print(f"\n\n\n{fg(210)}This Tools 💞Help💞 🥷Penetration🥷Testers🥷 in Recon SubDomains For 💣Target💣 {attr(0)} [SubEvil] 💯💯")
update()
time.sleep(3)
system()