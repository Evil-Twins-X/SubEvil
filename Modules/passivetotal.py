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

def passivetotal(Domains,useragent=useragent()):
    subdomains = []
    auth = (passivetotal_api_key, passivetotal_api_secret)
    response = requests.get(f"https://api.passivetotal.org/v2/enrichment/subdomains?query={Domains}",
                            auth=auth, stream=True,verify=True,headers={"User-Agent":useragent},timeout=15)
    data = json.loads(response.text)
    for sub in data["subdomains"]:
        if not subdomains.__contains__(sub + "." + Domains):
            subdomains.append(sub + "." + Domains)
    return subdomains