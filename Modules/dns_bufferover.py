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
def dns_bufferover(Domains,useragent=useragent()):
    subdomains = []
    response = requests.get(f"https://dns.bufferover.run/dns?q=.{Domains}", stream=True,verify=True,headers={'User-Agent':useragent},timeout=15)
    data = json.loads(response.text)
    for line in data["FDNS_A"]:
        sub = line.split(",")[1]
        if not subdomains.__contains__(sub):
            subdomains.append(sub)
    return subdomains