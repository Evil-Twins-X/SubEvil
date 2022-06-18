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
def tls_bufferover(Domains,useragent=useragent()):
    subdomains = []
    response = requests.get(f"https://tls.bufferover.run/dns?q=.{Domains}", stream=True,verify=True,headers={"User-Agent":useragent})
    data = json.loads(response.text)
    for line in data["Results"]:
        sub = line.split(",")[2]
        if not sub.startswith('*') and not subdomains.__contains__(sub):
            subdomains.append(sub)
    return subdomains