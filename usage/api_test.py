import json, requests, sys
import socket, urllib3, time
import os, random, threading
from time import time as tom
headers = {'Content-Type': 'application/json',
           'Authorization': '{0}'.format('null')}
cnt=(0)
ping=(0)
count=(0)
threads=(0)
working=(0)
loop=(True)
not_working=(0)
try:
    if sys.argv[1]:
        maxThreads=(int(sys.argv[1]))
    else:
        maxThreads=(10)
except Exception:
    maxThreads=(10)
def getProxy(proxType):
    global cnt, ping, count, threads, working, loop, not_working
    api_url = '{0}{1}'.format("https://proxy.soteria.cf/", proxType)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
def check(proxy, proxType, url):
    global cnt, ping, count, threads, working, loop, not_working
    try:
        bef = tom()
        requests.get(url,proxies={''+proxType:proxType+'://'+proxy},timeout=(5,10))
        aft = tom()
        ping=str(aft-bef)
        working+=(1)
        return "Working!"
    except Exception:
        not_working+=(1)
        aft = tom()
        ping=str(aft-bef)
        return "Not Working!"
def run(n):
    global cnt, ping, count, threads, working, loop, not_working
    try:
        ping=(0)
        magic=(random.randint(1,4))
        if (magic==1):
            try:
                count+=(1)
                http = getProxy('http')
                print(" [Thread-"+str(n+1)+"]    HTTP = "+http[0]+":"+http[1]+" | "+str(check(http[0]+":"+http[1],'http',"http://www.google.com/"))+" | "+str(ping)+"                ")
                cnt+=(1)
            except Exception:
                print(" [Thread-"+str(n+1)+"]    HTTP = Malformed Proxy Error    ")
        if (magic==2):
            try:
                count+=(1)
                https = getProxy('https')
                print(" [Thread-"+str(n+1)+"]    HTTPS = "+https[0]+":"+https[1]+" | "+str(check(https[0]+":"+https[1],'http',"https://www.google.com/"))+" | "+str(ping)+"          ")
                cnt+=(1)
            except Exception:
                print(" [Thread-"+str(n+1)+"]    HTTPS = Malformed Proxy Error   ")
        if (magic==3):
            try:
                count+=(1)
                socks4 = getProxy('socks4')
                print(" [Thread-"+str(n+1)+"]    Socks4 = "+socks4[0]+":"+socks4[1]+" | "+str(check(socks4[0]+":"+socks4[1],'socks4',"https://www.google.com/"))+" | "+str(ping)+"    ")
                cnt+=(1)
            except Exception:
                print(" [Thread-"+str(n+1)+"]    Socks4 = Malformed Proxy Error  ")
        if (magic==4):
            try:
                count+=(1)
                socks5 = getProxy('socks5')
                print(" [Thread-"+str(n+1)+"]    Socks5 = "+socks5[0]+":"+socks5[1]+" | "+str(check(socks5[0]+":"+socks5[1],'socks5',"https://www.google.com/"))+" | "+str(ping)+"    ")
                cnt+=(1)
            except Exception:
                print(" [Thread-"+str(n+1)+"]    Socks5 = Malformed Proxy Error  ")
    except KeyboardInterrupt:
        return
def finish():
    global cnt, ping, count, threads, working, loop, not_working, befTime
    try:
        while (loop):
            while (cnt == maxThreads):
                aftTime = tom()
                print(" \r\n")
                print("     [#] Finished Proxy API Analysis in "+str(aftTime-befTime)+"    ")
                print("     [#] "+str(working)+" working and "+str(not_working)+" not working   ")
                print("     [#] out of "+str(not_working+working)+" tested! ")
                print("\r\n ")
                cnt+=(1)
                loop=(False)
                return
            else:
                pass
    except KeyboardInterrupt:
        return
try:
    os.system('cls' if os.name=='nt' else 'clear')
    print("""\r\n
        /---------------------------------------------\\
        |   Just Showing off my blazing fast API :P   |
        \\---------------------------------------------/\
    """)
    print("\r\n ")
    print("     [#]  Starting Proxy API Analysis... (ctrl+c to stop)    ")
    print(" \r\n")
    while (threads < maxThreads):
        befTime = tom()
        threading.Thread(target=run, args=(threads,)).start()
        threads+=(1)
    else:
        threading.Thread(target=finish).start()
    exit
except KeyboardInterrupt:
    loop=(False)
    print(" \r\n")
    print("     [#]  Force Stopped Proxy API Analysis!  ")
    print("     [#] "+str(working)+" working and "+str(not_working)+" not working   ")
    print("     [#] out of "+str(not_working+working)+" tested! ")
    print("\r\n ")
    exit
