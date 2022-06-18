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
def threatminer(Domains,useragent=useragent()):
    try:
        url = f"https://api.threatminer.org/v2/domain.php?q={Domains}&rt=5"
        req = requests.get(url=url,verify=True,headers={"User-Agent":useragent})
        if '"status_code":"200"' in req.json():
            resp = req.json()['results']
            return resp
        else:
            pass
    except:
        pass