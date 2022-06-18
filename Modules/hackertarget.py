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
def hackertarget(Domains,useragent=useragent()):
    try:
        url = f"https://api.hackertarget.com/hostsearch/?q={Domains}"
        req = requests.get(url=url,verify=True,headers={"User-Agent":useragent})
        if Domains in req.text:
            resp = req.text
            s = []
            for i in resp.splitlines():
                s.append(i)
            return s
        else:
            pass
    except:
        pass