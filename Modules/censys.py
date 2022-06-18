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

def censys(Domain,useragent=useragent()):
    subdomains = []
    page = pages = 1
    while page <= pages:
        headers = {"Content-Type": "application/json", "Accept": "application/json","User-agent":useragent}
        auth = (censys_api_id, censys_api_secret)
        data = {"query": Domain, "page": page, "fields": ["parsed.names"]}
        response = requests.post("https://www.censys.io/api/v1/search/certificates",
                                 headers=headers, json=data, auth=auth, stream=True)
        data = json.loads(response.text)
        pages = data["metadata"]["pages"]
        for res in data["results"]:
            pn = res["parsed.names"]
            for sub in pn:
                sub = sub.replace("http://", "")
                sub = sub.replace("https://", "")
                if "." + Domain in sub and not sub.startswith("*") and not subdomains.__contains__(sub):
                    subdomains.append(sub)
        page = page + 1
    return subdomains