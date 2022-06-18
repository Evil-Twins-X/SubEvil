"""
███████╗██╗   ██╗██████╗ ███████╗██╗   ██╗██╗██╗     
██╔════╝██║   ██║██╔══██╗██╔════╝██║   ██║██║██║     
███████╗██║   ██║██████╔╝█████╗  ██║   ██║██║██║     
╚════██║██║   ██║██╔══██╗██╔══╝  ╚██╗ ██╔╝██║██║     
███████║╚██████╔╝██████╔╝███████╗ ╚████╔╝ ██║███████╗
╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝  ╚═══╝  ╚═╝╚══════╝
#=====================================================
#           Tool  Version : V 1.1.2
#           Programmer    : EvilTwins
#           Facebook      : @evi1.twins
#           Github        : @Evi1-Back
#======================================================
"""
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
#-----------------------------#
from colored import fg,attr
import time
import sys
import os
import argparse
import threading
from multiprocessing import Pool
import argparse
#------------------------------#
parser = argparse.ArgumentParser()
parser.add_argument('--domains','-d', type=str,help="Domain name to enumerate it's subdomains")
parser.add_argument("--random-agent",'-ra',help="Use randomly selected HTTP User-Agent header value",action='store_true')
parser.add_argument("--version",'-v',help="Show program's version number and exit",action='store_true')
parser.add_argument("--update",help="update SubEvil [Please update the tool every Saturday]",action='store_true')    
args = parser.parse_args()
#-----------------------------#
versions = "V1.1.2"
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
print(f"\n\n\n{fg(210)}This Tools 💞Help💞 🥷Penetration🥷Testers🥷 in Recon SubDomains For 💣Target💣 {attr(0)} [SubEvil] 💯💯")
time.sleep(2)
system()
print(Brand(versions))
#---------------------------#
domains =  args.domains
if domains == None:
    exit(0)
ListSubdomains = []
print(f"{fg(1)}Target{attr(0)} 💣 {domains} 💣")
#---------------------------#
def addDomainsAlienvault():
    try:
        th = alienvault(domains)
        for i in th:
            if not ListSubdomains.__contains__(i):
                ListSubdomains.append(i)
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
            if "," in i:
                s = i.split(",")[0]
                print(s)
            else:
                print(i)
        else:
            pass
    print(f"{fg(8)}Subdomains Fund{attr(0)} [{N}]")

Start()
