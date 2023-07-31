import socket
from multiprocessing import Pool
from colored import Fore,Style
def scan_port(data):
    try:
        splits = data.split(":")
        ip = splits[0]
        ports = splits[1].split(",")
        openport = []
        for port in ports :
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  
            result = sock.connect_ex((str(ip), int(port)))
            if result == 0:
                openport.append(f"{Fore.green}{port}{Style.reset}")
            sock.close()
        if len(openport) == 0 :
            pass
        else: 
            print(ip,f' ,'.join(openport))
    except:
        pass
    