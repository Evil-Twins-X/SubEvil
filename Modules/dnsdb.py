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


def dnsdb(Domains,useragent=useragent()):
    subdomains = []
    headers = {"Accept": "application/json", "Content-Type": "application/json", "X-API-Key": dnsdb_api_key,"User-Agent":useragent}
    response = requests.get(f"https://api.dnsdb.info/lookup/rrset/name/*.{Domains}?limit=1000000000",
                            headers=headers, stream=True,verify=True,timeout=15)
    for line in response.text.split("\n"):
        if line == "":
            continue
        sub = json.loads(line)["rrname"]
        sub = sub.rstrip(".")
        if "_" not in sub and not subdomains.__contains__(sub):
            subdomains.append(sub)
    return subdomains