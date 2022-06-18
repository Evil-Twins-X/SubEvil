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


def facebook(Domains,useragent=useragent()):
    subdomains =[]
    response = requests.get(
        f"https://graph.facebook.com/certificates?query={Domains}&fields=domains&limit=10000&access_token={facebook_access_token}",
        stream=True,verify=True,headers={"User-Agent":useragent})
    data = json.loads(response.text)
    for res in data["data"]:
        for sub in res["domains"]:
            if not sub.startswith('*') and not subdomains.__contains__(sub):
                subdomains.append(sub)
    return subdomains