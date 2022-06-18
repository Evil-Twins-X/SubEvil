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


def securitytrails(Domains,useragent=useragent()):
    subdomains = []
    headers = {"apikey": securitytrails_API,"User-Agent":useragent}
    response = requests.get(f"https://api.securitytrails.com/v1/domain/{Domains}/subdomains",
                            headers=headers, stream=True)
    data = json.loads(response.text)
    for sub in data["subdomains"]:
        if not subdomains.__contains__(sub + "." + Domains):
            subdomains.append(sub + "." + Domains)
    return subdomains