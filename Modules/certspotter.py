import requests
import json
from Lib.userAgent import useragent
from Lib.Configer import *
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
def certspotter(Domains,useragent=useragent()):
    headers = {"Authorization": f"Bearer {certspotter_api_key}",'User-Agent':useragent}
    response = requests.get(f"https://api.certspotter.com/v1/issuances?domain={Domains}&expand=dns_names",
                            headers=headers, stream=True ,verify=True)
    subdomains = []
    data = json.loads(response.text)
    for dns_names in data:
        for dns_name in dns_names["dns_names"]:
            if not dns_name.startswith('*') and not subdomains.__contains__(dns_name):
                subdomains.append(dns_name)
    return subdomains