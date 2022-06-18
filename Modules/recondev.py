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

def recondev(Domains,useragent=useragent()):
    subdomains = []
    response = requests.get(f"https://recon.dev/api/search?key={recondev_api_key}&domain={Domains}", stream=True,verify=True,headers={'User-Agent':useragent})
    data = json.loads(response.text)
    for res in data:
        for sub in res["rawDomains"]:
            if not sub.startswith('*') and "." + Domains in sub and not subdomains.__contains__(sub):
                subdomains.append(sub)
    return subdomains