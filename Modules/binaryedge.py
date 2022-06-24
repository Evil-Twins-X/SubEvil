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


def binaryedge(Domains,useragent=useragent()):
    subdomains = []
    page = pages = 1
    while page <= pages:
        headers = {"X-Key": binaryedge_api_key,"User-Agent":useragent}
        response = requests.get(f"https://api.binaryedge.io/v2/query/domains/subdomain/{Domains}?page={page}",
                                headers=headers, stream=True,verify=True,timeout=15)
        data = json.loads(response.text)
        pages = data["pagesize"]
        for sub in data["events"]:
            if not subdomains.__contains__(sub):
                subdomains.append(sub)
        page = page + 1
    return subdomains