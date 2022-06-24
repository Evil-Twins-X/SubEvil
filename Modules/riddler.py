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


def riddler(Domains,useragent=useragent()):
    subdomains = []
    response = requests.get(f"https://riddler.io/search/exportcsv?q=pld:{Domains}", stream=True,verify=True,headers={"User-Agent":useragent},timeout=15)
    data = csv.reader(line.decode('utf-8') for line in response.iter_lines())
    next(data)
    next(data)
    for row in data:
        if not subdomains.__contains__(row[4]):
            subdomains.append(row[4])
    return subdomains