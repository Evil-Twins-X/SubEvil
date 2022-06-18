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


def whoisxmlapi(Domains,useragent=useragent()):
    subdomains = []
    response = requests.get(
        f"https://subdomains.whoisxmlapi.com/api/v1?apiKey={whoisxmlapi_api_key}&domainName={Domains}", 
        stream=True,verify=True,headers={"User-Agent":useragent})
    data = json.loads(response.text)
    for res in data["result"]["records"]:
        sub = res["domain"]
        if not subdomains.__contains__(sub):
            subdomains.append(sub)
    return subdomains