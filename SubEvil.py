"""
███████╗██╗   ██╗██████╗ ███████╗██╗   ██╗██╗██╗     
██╔════╝██║   ██║██╔══██╗██╔════╝██║   ██║██║██║     
███████╗██║   ██║██████╔╝█████╗  ██║   ██║██║██║     
╚════██║██║   ██║██╔══██╗██╔══╝  ╚██╗ ██╔╝██║██║     
███████║╚██████╔╝██████╔╝███████╗ ╚████╔╝ ██║███████╗
╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝  ╚═══╝  ╚═╝╚══════╝
#=====================================================
#           Tool  Version : V 1.1.1
#           Programmer    : EvilTwins
#           Facebook      : @evi1.twins
#           Github        : @Evi1-Back
#======================================================
"""
from ast import For
import http
from Modules.alienvault import alienvault
from Modules.anubis import anubis
from Modules.binaryedge import binaryedge
from Modules.censys import censys
from Modules.certspotter import certspotter
from Modules.crt import crt
from Modules.dns_bufferover import dns_bufferover
from Modules.dnsdb import dnsdb
from Modules.facebook import facebook
from Modules.hackertarget import hackertarget
from Modules.omnisint import omnisint
from Modules.passivetotal import passivetotal
from Modules.riddler import riddler
from Modules.securitytrails import securitytrails
from Modules.shodan import shodan
from Modules.spyse import spyse
from Modules.sublist3r import sublist3r
from Modules.threatcrowd import threatcrowd
from Modules.threatminer import threatminer
from Modules.tls_bufferover import tls_bufferover
from Modules.urlscan import urlscan
from Modules.virustotal import virustotal
from Modules.whoisxmlapi import whoisxmlapi
from Modules.recondev import recondev
#-----------------------------#
from Lib.Brand import *
from Lib.HttpORHttps import Http
from Lib.HttpORHttps import Https
from Lib.PortScanner import scan_port
#-----------------------------#
from colored import Style , Fore
import time
import sys
import os
import argparse
import threading
from multiprocessing import Pool
import argparse
versions = "V2.1.1"
print(Brand(versions))
#------------------------------#
parser = argparse.ArgumentParser()
parser.add_argument('--domains','-d', type=str,help="Domain name to enumerate it's subdomains")
parser.add_argument("--port-scan",'-p',type=str,help="  " )
parser.add_argument("--random-agent",'-ra',help="Use randomly selected HTTP User-Agent header value",action='store_true')
parser.add_argument("--version",'-v',help="Show program's version number and exit",action='store_true')
parser.add_argument("--http-only","-http",help="Test Domains Ony HTTP",action='store_true')
parser.add_argument("--https-only","-https",help="Test Domains Ony HTTPS",action='store_true')
parser.add_argument("--status-code",'-sc',type=str,help="display response status-code --status-code All or 200 or 404 or 303 etc.." )
parser.add_argument("--title",'-t',help="display page title",action='store_true')
parser.add_argument("--update",help="update SubEvil [Please update the tool every Saturday]",action='store_true')    
args = parser.parse_args()
#-----------------------------#
def system():
    os.system('cls' if os.name == 'nt' else 'clear')
#--------------------------#
if args.version :
    print(f"💯 SubEvil version {versions}")
    exit(0)
if args.update:
    os.system(f"python Update.py {versions}")
    exit(0)
#---------------------------#
system()
print(Brand(versions))
print(f"\n\n\n{Fore.blue}This Tools 💞Help💞 🥷Penetration🥷Testers🥷 in Recon SubDomains For 💣Target💣 {Style.reset} [{Fore.green}SubEvil{Style.reset}] 💯💯")
time.sleep(2)
system()
print(Brand(versions))
#---------------------------#
domains =  args.domains
if domains == None:
    exit(0)
ListSubdomains = []
print(f"{Fore.red}Target{Style.reset} 💣 {domains} 💣")
if args.http_only and args.https_only:
    print(f"{Fore.red} \n      You Cannot Use --http-only And --https-Only must choose only one")
    exit(0)
if args.status_code or args.title:
    if args.https_only or args.http_only:
        pass
    else:
        print(f"{Fore.red}         You cannot use --title  or  --status-code without using  --https-Only or  --http-Only")
        exit(0)
#---------------------------#
def addDomainsAlienvault():
    try:
        th = alienvault(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
                if domains in i:
                    if "," in i:
                        s = i.split(",")[0]
                        print(s)
                    else:
                        print(i)
                else:
                    pass
            else:
                pass
    except:
        pass
def addDomainsAnubis():
    try:
        th = anubis(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
                if domains in i:
                    if "," in i:
                        s = i.split(",")[0]
                        print(s)
                    else:
                        print(i)
                else:
                    pass
            else:
                pass
    except:
        pass
def addDomainsBinaryedge():
    try:
        th = binaryedge(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
                if domains in i:
                    if "," in i:
                        s = i.split(",")[0]
                        print(s)
                    else:
                        print(i)
                else:
                    pass
            else:
                pass
    except:
        pass
def addDomainsCensys():
    try:
        th = censys(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
                if domains in i:
                    if "," in i:
                        s = i.split(",")[0]
                        print(s)
                    else:
                        print(i)
                else:
                    pass
            else:
                pass
    except:
        pass
def addDomainsCertspotter():
    try:
        th = certspotter(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
                if domains in i:
                    if "," in i:
                        s = i.split(",")[0]
                        print(s)
                    else:
                        print(i)
                else:
                    pass
            else:
                pass
    except:
        pass
def addDomainsCrt():
    try:
        th = crt(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
                if domains in i:
                    if "," in i:
                        s = i.split(",")[0]
                        print(s)
                    else:
                        print(i)
                else:
                    pass
            else:
                pass
    except:
        pass
def addDomainsDns_bufferover():
    try:
        th = dns_bufferover(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
                if domains in i:
                    if "," in i:
                        s = i.split(",")[0]
                        print(s)
                    else:
                        print(i)
                else:
                    pass
            else:
                pass
    except:
        pass
def addDomainsDnsdb():
    try:
        th = dnsdb(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
                if domains in i:
                    if "," in i:
                        s = i.split(",")[0]
                        print(s)
                    else:
                        print(i)
                else:
                    pass
            else:
                pass
    except:
        pass
def addDomainsFacebook():
    try:
        th = facebook(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
                if domains in i:
                    if "," in i:
                        s = i.split(",")[0]
                        print(s)
                    else:
                        print(i)
                else:
                    pass
            else:
                pass
    except:
        pass
def addDomainsHackertarget():
    try:
        th = hackertarget(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
                if domains in i:
                    if "," in i:
                        s = i.split(",")[0]
                        print(s)
                    else:
                        print(i)
                else:
                    pass
            else:
                pass
    except:
        pass
def addDomainsOmnisint():
    try:
        th = omnisint(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
                if domains in i:
                    if "," in i:
                        s = i.split(",")[0]
                        print(s)
                    else:
                        print(i)
                else:
                    pass
            else:
                pass
    except:
        pass
def addDomainsPassivetotal():
    try:
        th = passivetotal(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
                if domains in i:
                    if "," in i:
                        s = i.split(",")[0]
                        print(s)
                    else:
                        print(i)
                else:
                    pass
            else:
                pass
    except:
        pass
def addDomainsRiddler():
    try:
        th = riddler(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
                if domains in i:
                    if "," in i:
                        s = i.split(",")[0]
                        print(s)
                    else:
                        print(i)
                else:
                    pass
            else:
                pass
    except:
        pass
def addDomainsSecuritytrails():
    try:
        th = securitytrails(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
                if domains in i:
                    if "," in i:
                        s = i.split(",")[0]
                        print(s)
                    else:
                        print(i)
                else:
                    pass
            else:
                pass
    except:
        pass
def addDomainsShodan():
    try:
        th = shodan(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
                if domains in i:
                    if "," in i:
                        s = i.split(",")[0]
                        print(s)
                    else:
                        print(i)
                else:
                    pass
            else:
                pass
    except:
        pass
def addDomainsSpyse():
    try:
        th = spyse(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
                if domains in i:
                    if "," in i:
                        s = i.split(",")[0]
                        print(s)
                    else:
                        print(i)
                else:
                    pass
            else:
                pass
    except:
        pass
def addDomainsSublist3r():
    try:
        th = sublist3r(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
                if domains in i:
                    if "," in i:
                        s = i.split(",")[0]
                        print(s)
                    else:
                        print(i)
                else:
                    pass
            else:
                pass
    except:
        pass
def addDomainsThreatcrowd():
    try:
        th = threatcrowd(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
                if domains in i:
                    if "," in i:
                        s = i.split(",")[0]
                        print(s)
                    else:
                        print(i)
                else:
                    pass
            else:
                pass
    except:
        pass
def addDomainsThreatminer():
    try:
        th = threatminer(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
                if domains in i:
                    if "," in i:
                        s = i.split(",")[0]
                        print(s)
                    else:
                        print(i)
                else:
                    pass
            else:
                pass
    except:
        pass
def addDomainsTls_bufferover():
    try:
        th = tls_bufferover(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
                if domains in i:
                    if "," in i:
                        s = i.split(",")[0]
                        print(s)
                    else:
                        print(i)
                else:
                    pass
            else:
                pass
    except:
        pass
def addDomainsUrlscan():
    try:
        th = urlscan(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
                if domains in i:
                    if "," in i:
                        s = i.split(",")[0]
                        print(s)
                    else:
                        print(i)
                else:
                    pass
            else:
                pass
    except:
        pass
def addDomainsVirustotal():
    try:
        th = virustotal(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
                if domains in i:
                    if "," in i:
                        s = i.split(",")[0]
                        print(s)
                    else:
                        print(i)
                else:
                    pass
            else:
                pass
    except:
        pass
def addDomainsWhoisxmlapi():
    try:
        th = whoisxmlapi(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
                if domains in i:
                    if "," in i:
                        s = i.split(",")[0]
                        print(s)
                    else:
                        print(i)
                else:
                    pass
            else:
                pass
    except:
        pass
def addDomainsRecondev():
    try:
        th = recondev(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
                if domains in i:
                    if "," in i:
                        s = i.split(",")[0]
                        print(s)
                    else:
                        print(i)
                else:
                    pass               
            else:
                pass
    except:
        pass
def run():
    threading.Thread(addDomainsAlienvault()).start()
    threading.Thread(addDomainsAnubis()).start()
    threading.Thread(addDomainsBinaryedge()).start()
    threading.Thread(addDomainsCensys()).start()
    threading.Thread(addDomainsCertspotter()).start()
    threading.Thread(addDomainsCrt()).start()
    threading.Thread(addDomainsDns_bufferover()).start()
    threading.Thread(addDomainsDnsdb()).start()
    threading.Thread(addDomainsFacebook()).start()
    threading.Thread(addDomainsHackertarget()).start()
    threading.Thread(addDomainsOmnisint()).start()
    threading.Thread(addDomainsPassivetotal()).start()
    threading.Thread(addDomainsRiddler()).start()
    threading.Thread(addDomainsSecuritytrails()).start()
    threading.Thread(addDomainsShodan()).start()
    threading.Thread(addDomainsSpyse()).start()
    threading.Thread(addDomainsSublist3r()).start()
    threading.Thread(addDomainsThreatcrowd()).start()
    threading.Thread(addDomainsThreatminer()).start()
    threading.Thread(addDomainsTls_bufferover()).start()
    threading.Thread(addDomainsUrlscan()).start()
    threading.Thread(addDomainsVirustotal()).start()
    threading.Thread(addDomainsWhoisxmlapi()).start()
    threading.Thread(addDomainsRecondev()).start()
def Start():
    threading.Thread(run()).start()
    N = 0
    for i in ListSubdomains:
        if domains in i:
            N+=1
        else:
            pass
    print(f"{Fore.blue}Subdomains Fund{Style.reset} [{N}]")
Start()
if args.http_only:
    httponly = True
else:
    httponly = False
if args.https_only:
    httpsonly = True
else:
    httpsonly = False
if args.status_code:
    status_code =  args.status_code
else:
    status_code = False
if args.title:
    title = True
else:
    title = False
def http_(Target):
    Http(Target=Target,HTTP=httponly,Title=title,StatusCode=status_code)
def https_(Target):
    Https(Target=Target,HTTPs=httpsonly,Title=title,StatusCode=status_code)
if args.http_only:
    pool = Pool(120)
    pool.map(http_,ListSubdomains)
    pool.close()
    pool.join()
else:
    pass
if args.https_only:
    pool = Pool(120)
    pool.map(https_,ListSubdomains)
    pool.close()
    pool.join()
else:
    pass
if args.port_scan:
    data = []
    for i in ListSubdomains:
        data.append(f'{i}:{args.port_scan}')
    pool = Pool(40)
    pool.map(scan_port, data)
    pool.close()
    pool.join()
