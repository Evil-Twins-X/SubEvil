import requests
import json
from Lib.Configer import *
from Lib.userAgent import useragent
"""
███████╗██╗   ██╗██████╗ ███████╗██╗   ██╗██╗██╗     
██╔════╝██║   ██║██╔══██╗██╔════╝██║   ██║██║██║     
███████╗██║   ██║██████╔╝█████╗  ██║   ██║██║██║     
╚════██║██║   ██║██╔══██╗██╔══╝  ╚██╗ ██╔╝██║██║     
███████║╚██████╔╝██████╔╝███████╗ ╚████╔╝ ██║███████╗
╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝  ╚═══╝  ╚═╝╚══════╝
#=====================================================
#           Tool  Version : V 1.0
#           Programmer    : Evil-Twins
#           Facebook      : @evi1.twins
#           Github        : @Evil-Twins-X
#======================================================
"""

def crt(Domains,useragent=useragent()):
    subdomains = []
    response = requests.get(f"https://crt.sh/?q={Domains}&output=json", stream=True,verify=True,headers={"User-Agent":useragent},timeout=15)
    data = json.loads(response.text)
    for res in data:
        for sub in res["name_value"].split("\n"):
            if not sub.startswith('*') and not subdomains.__contains__(sub):
                subdomains.append(sub)
    return subdomains
