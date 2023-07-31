import requests
import os
import sys
from Lib.Brand import *
from  colored import Fore,Style
import time
def system():
    os.system('cls' if os.name == 'nt' else 'clear')
def update(version=sys.argv[1]):
    CheckUpdate = "https://raw.githubusercontent.com/Evil-Twins-X/MyToolsUpdate/main/SubEvil.txt"
    req = requests.get(url=CheckUpdate).text
    if version in req :
        print(f"{Fore.green}✅💯 The tool is updated ✅💯{Style.reset}")
    else: 
        for i in req.splitlines():
            if ".py" in i:
                print(f"{Fore.green} This file needs updating [{i}] {Style.reset}")
                urlGetupdate = f"https://raw.githubusercontent.com/Evil-Twins-X/SubEvil/main/{i}"
                try:
                    os.remove(f"{i}")
                except:
                    pass
                textfile =requests.get(urlGetupdate).text
                open(f"{i}",'a').write(textfile)
system()
print(Brand(sys.argv[1]))
print("Wite Check For Update ")
print(f"\n\n\n{Fore.blue}This Tools 💞Help💞 🥷Penetration🥷Testers🥷 in Recon SubDomains For 💣Target💣 {Style.reset} [SubEvil] 💯💯")
update()
