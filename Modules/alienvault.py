from cgitb import reset
import re
from urllib import response
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
import requests
from Lib.userAgent import useragent
def alienvault(Domains,useragent=useragent()):
    try:
        url = f"https://otx.alienvault.com/api/v1/indicators/domain/{Domains}/passive_dns"
        req = requests.get(url=url,verify=True,headers={"User-Agent":useragent})
        if Domains in req.json():
            resp = req.json()['passive_dns']['hostname']
            return resp
        else:
            pass
    except:
        pass