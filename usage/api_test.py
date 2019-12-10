import json, requests, socket, urllib3, os, random
from threading import Thread
from time import time
headers = {'Content-Type': 'application/json',
           'Authorization': '{0}'.format('null')}
ping=(0)
working=(0)
not_working=(0)
def getProxy(proxType):
    api_url = '{0}{1}'.format("https://proxy.soteria.cf/", proxType)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
def check(proxy, proxType, url):
    global ping
    global working
    global not_working
    try:
        bef = time()
        requests.get(url,proxies={''+proxType:proxType+'://'+proxy},timeout=(3.05,27))
        aft = time()
        ping=str(aft-bef)
        working+=(1)
        return "Working!"
    except Exception:
        not_working+=(1)
        return "Not Working!"
try:
    os.system('cls' if os.name=='nt' else 'clear')
    print("""\r\n
        /---------------------------------------------\\
        |   Just Showing off my blazing fast API :P   |
        \\---------------------------------------------/\
    """)
    print("\r\n")
    print("     [#]  Starting Proxy API Analysis... (ctrl+c to stop)")
    count=(0)
    while (1==1):
        ping=(0)
        magic=(random.randint(1,4))
        if (magic==1):
            try:
                count+=(1)
                http = getProxy('http')
                print(" ["+str(count)+"]    HTTP = "+http[0]+":"+http[1]+" | "+str(check(http[0]+":"+http[1],'http',"http://www.google.com/"))+" | "+str(ping))
            except Exception:
                print(" ["+str(count)+"]    HTTP = Malformed Proxy Error")
        if (magic==2):
            try:
                count+=(1)
                https = getProxy('https')
                print(" ["+str(count)+"]    HTTPS = "+https[0]+":"+https[1]+" | "+str(check(https[0]+":"+https[1],'http',"https://www.google.com/"))+" | "+str(ping))
            except Exception:
                print(" ["+str(count)+"]    HTTPS = Malformed Proxy Error")
        if (magic==3):
            try:
                count+=(1)
                socks4 = getProxy('socks4')
                print(" ["+str(count)+"]    Socks4 = "+socks4[0]+":"+socks4[1]+" | "+str(check(socks4[0]+":"+socks4[1],'socks4',"https://www.google.com/"))+" | "+str(ping))
            except Exception:
                print(" ["+str(count)+"]    Socks4 = Malformed Proxy Error")
        if (magic==4):
            try:
                count+=(1)
                socks5 = getProxy('socks5')
                print(" ["+str(count)+"]    Socks5 = "+socks5[0]+":"+socks5[1]+" | "+str(check(socks5[0]+":"+socks5[1],'socks5',"https://www.google.com/"))+" | "+str(ping))
            except Exception:
                print(" ["+str(count)+"]    Socks5 = Malformed Proxy Error")
except KeyboardInterrupt:
    print("\r\n")
    print("     [#]  Finished Proxy API Analysis! ")
    print("     [#] "+str(working)+" working and "+str(not_working)+" not working")
    print("     [#] out of "+str(not_working+working)+" tested!")
    print("\r\n")
    exit
