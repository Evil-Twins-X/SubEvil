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


def virustotal(Domains,useragent=useragent()):
    subdomains = []
    headers = {"x-apikey": virustotal_api_key,"User-Agent":useragent}
    response = requests.get(f"https://www.virustotal.com/api/v3/domains/{Domains}/subdomains",
                            headers=headers, stream=True)
    data = json.loads(response.text)
    for sub in data["data"]:
        if not subdomains.__contains__(sub["id"]):
            subdomains.append(sub["id"])
    return subdomains