from ast import Pass
from posixpath import split
import requests
from lxml.html import fromstring
from colored import fg,attr
def Http(Target,HTTP,Title,StatusCode):
    try:
        if HTTP   == True:
            url = f"http://{Target}"
            req =requests.get(url,timeout=5)
            Pro = []
            Pro.append(url)
            if Title == False and StatusCode == False :
                pass
            elif Title == True :
                try:
                    tree = fromstring(req.content)
                    tree.findtext('.//title')
                    Pro.append(f"{fg(40)}[{attr(0)}{tree.findtext('.//title')}{fg(40)}]{attr(0)}")
                except:
                    Pro.append(f"{fg(2)}[{attr(0)} Not Title{fg(2)}]{attr(0)}")
            if StatusCode == False :
                pass 
            else:
                status = req.status_code
                if StatusCode == "All" or  StatusCode == "all":
                    if status  == 200:
                        Pro.append(f"[ {fg(40)}{status}{attr(0)} ]")
                    else:
                        Pro.append(f"[ {fg(1)}{status}{attr(0)} ]")
                elif ',' in str(StatusCode):
                    s = StatusCode.split(',')
                    if len(s) == 2 :
                        if s[0] == str(status)  == "200":
                            Pro.append(f"[ {fg(40)}{status}{attr(0)} ]")
                        else:
                            if s[0] == str(status):
                                Pro.append(f"[ {fg(1)}{status}{attr(0)} ]")
                        if s[1] == str(status)  == "200":
                            Pro.append(f"[ {fg(40)}{status}{attr(0)} ]")
                        else:
                            if s[1] == str(status):
                                Pro.append(f"[ {fg(1)}{status}{attr(0)} ]")
                    if len(s) == 3 :
                        if s[0] == str(status)  == "200":
                            Pro.append(f"[ {fg(40)}{status}{attr(0)} ]")
                        else:
                            if s[0] == str(status):
                                Pro.append(f"[ {fg(1)}{status}{attr(0)} ]")
                        if s[1] == str(status)  == "200":
                            Pro.append(f"[ {fg(40)}{status}{attr(0)} ]")
                        else:
                            if s[1] == str(status):
                                Pro.append(f"[ {fg(1)}{status}{attr(0)} ]") 
                        if s[2] == str(status)  == "200":
                            Pro.append(f"[ {fg(40)}{status}{attr(0)} ]")
                        else:
                            if s[2] == str(status):
                                Pro.append(f"[ {fg(1)}{status}{attr(0)} ]")
                    if len(s) == 4 :
                        if s[0] == str(status)  == "200":
                            Pro.append(f"[ {fg(40)}{status}{attr(0)} ]")
                        else:
                            if s[0] == str(status):
                                Pro.append(f"[ {fg(1)}{status}{attr(0)} ]")
                        if s[1] == str(status)  == "200":
                            Pro.append(f"[ {fg(40)}{status}{attr(0)} ]")
                        else:
                            if s[1] == str(status):
                                Pro.append(f"[ {fg(1)}{status}{attr(0)} ]") 
                        if s[2] == str(status)  == "200":
                            Pro.append(f"[ {fg(40)}{status}{attr(0)} ]")
                        else:
                            if s[2] == str(status):
                                Pro.append(f"[ {fg(1)}{status}{attr(0)} ]")
                        if s[3] == str(status)  == "200":
                            Pro.append(f"[ {fg(40)}{status}{attr(0)} ]")
                        else:
                            if s[3] == str(status):
                                Pro.append(f"[ {fg(1)}{status}{attr(0)} ]")
                    if len(s) > 4 :
                        print("Can Use --status-code All")    
                elif int(status) == int(StatusCode):
                    if status  == 200:
                        Pro.append(f"[ {fg(40)}{status}{attr(0)} ]")
                    else:
                        Pro.append(f"[ {fg(1)}{status}{attr(0)} ]")
                else:
                    pass
            if len(Pro) == 3:
                print(f"{Pro[1]}  {Pro[2]} {Pro[0]}")
            elif  len(Pro) == 2:
                print(f"{Pro[1]} {Pro[0]} ")
            elif  len(Pro) == 1:
                if Title == False and StatusCode == False:
                    print(f"{Pro[0]}")
                else:
                    pass
            else:
                pass
        else:
            pass
    except:
        pass


def Https(Target,HTTPs,Title,StatusCode):
    try:
        if HTTP   == True:
            url = f"https://{Target}"
            req =requests.get(url,timeout=5)
            Pro = []
            Pro.append(url)
            if Title == False and StatusCode == False :
                pass
            elif Title == True :
                try:
                    tree = fromstring(req.content)
                    tree.findtext('.//title')
                    Pro.append(f"{fg(40)}[{attr(0)}{tree.findtext('.//title')}{fg(40)}]{attr(0)}")
                except:
                    Pro.append(f"{fg(2)}[{attr(0)} Not Title{fg(2)}]{attr(0)}")
            if StatusCode == False :
                pass 
            else:
                status = req.status_code
                if StatusCode == "All" or  StatusCode == "all":
                    if status  == 200:
                        Pro.append(f"[ {fg(40)}{status}{attr(0)} ]")
                    else:
                        Pro.append(f"[ {fg(1)}{status}{attr(0)} ]")
                elif ',' in str(StatusCode):
                    s = StatusCode.split(',')
                    if len(s) == 2 :
                        if s[0] == str(status)  == "200":
                            Pro.append(f"[ {fg(40)}{status}{attr(0)} ]")
                        else:
                            if s[0] == str(status):
                                Pro.append(f"[ {fg(1)}{status}{attr(0)} ]")
                        if s[1] == str(status)  == "200":
                            Pro.append(f"[ {fg(40)}{status}{attr(0)} ]")
                        else:
                            if s[1] == str(status):
                                Pro.append(f"[ {fg(1)}{status}{attr(0)} ]")
                    if len(s) == 3 :
                        if s[0] == str(status)  == "200":
                            Pro.append(f"[ {fg(40)}{status}{attr(0)} ]")
                        else:
                            if s[0] == str(status):
                                Pro.append(f"[ {fg(1)}{status}{attr(0)} ]")
                        if s[1] == str(status)  == "200":
                            Pro.append(f"[ {fg(40)}{status}{attr(0)} ]")
                        else:
                            if s[1] == str(status):
                                Pro.append(f"[ {fg(1)}{status}{attr(0)} ]") 
                        if s[2] == str(status)  == "200":
                            Pro.append(f"[ {fg(40)}{status}{attr(0)} ]")
                        else:
                            if s[2] == str(status):
                                Pro.append(f"[ {fg(1)}{status}{attr(0)} ]")
                    if len(s) == 4 :
                        if s[0] == str(status)  == "200":
                            Pro.append(f"[ {fg(40)}{status}{attr(0)} ]")
                        else:
                            if s[0] == str(status):
                                Pro.append(f"[ {fg(1)}{status}{attr(0)} ]")
                        if s[1] == str(status)  == "200":
                            Pro.append(f"[ {fg(40)}{status}{attr(0)} ]")
                        else:
                            if s[1] == str(status):
                                Pro.append(f"[ {fg(1)}{status}{attr(0)} ]") 
                        if s[2] == str(status)  == "200":
                            Pro.append(f"[ {fg(40)}{status}{attr(0)} ]")
                        else:
                            if s[2] == str(status):
                                Pro.append(f"[ {fg(1)}{status}{attr(0)} ]")
                        if s[3] == str(status)  == "200":
                            Pro.append(f"[ {fg(40)}{status}{attr(0)} ]")
                        else:
                            if s[3] == str(status):
                                Pro.append(f"[ {fg(1)}{status}{attr(0)} ]")
                    if len(s) > 4 :
                        print("Can Use --status-code All")    
                elif int(status) == int(StatusCode):
                    if status  == 200:
                        Pro.append(f"[ {fg(40)}{status}{attr(0)} ]")
                    else:
                        Pro.append(f"[ {fg(1)}{status}{attr(0)} ]")
                else:
                    pass
            if len(Pro) == 3:
                print(f"{Pro[1]}  {Pro[2]} {Pro[0]}")
            elif  len(Pro) == 2:
                print(f"{Pro[1]} {Pro[0]} ")
            elif  len(Pro) == 1:
                if Title == False and StatusCode == False:
                    print(f"{Pro[0]}")
                else:
                    pass
            else:
                pass
        else:
            pass
    except:
        pass