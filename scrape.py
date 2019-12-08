#!/usr/bin/python3
import requests, json, sys, sqlite3, os.path, random
from sqlalchemy import create_engine
from bs4 import BeautifulSoup
from sqlite3 import Error
def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
      if random.randrange(num): continue
      line = aline
    return line
proxies = {
 "http": random.choice(list(requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=2050&country=US&ssl=all&anonymity=all', timeout=10).text)),
}
if os.path.exists('proxies.db')==False:
    conn = sqlite3.connect('proxies.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE proxies ([ip] text, [port] text, [type] text)''')
    conn.commit()
db_connect = create_engine('sqlite:///proxies.db')
if len(sys.argv) >= 2:
    mass = True
else:
    mass = False
def add(self, ip, port, type):
    conn = db_connect.connect()
    conn.execute("insert into proxies values('{0}','{1}','{2}')".format(ip, port, type))
    return self+' added set for '+type
def source1(debug):
    page = (requests.get('http://pubproxy.com/api/proxy', timeout=10))
    soup = (BeautifulSoup(page.text, 'html.parser').text)
    if "maximum" in soup:
        return ''
    proxyData = (json.loads(soup))
    proxyMetaDED = (proxyData['data'])
    proxyMeta = (json.loads(json.dumps(proxyMetaDED[0])))
    proxySupDED = (proxyMeta['support'])
    proxySup = (json.loads(json.dumps(proxySupDED)))
    if (debug==1):
        print('         [Source 1 : Soteria Debug Log : START]')
        print('     [IP:PORT]   '+proxyMeta['ipPort'])
        print('     [TYPE]      '+proxyMeta['type'])
        print('     [COUNTRY]   '+proxyMeta['country'])
        print('     [CHECKED]   '+proxyMeta['last_checked'])
        print('     [LEVEL]     '+proxyMeta['proxy_level'])
        print('     [GOOGLE]    '+str(proxySup['google']))
        print('     [HTTPS]     '+str(proxySup['https']))
        print('     [PING]      '+proxyMeta['speed'])
        print('         [Source 1 : Soteria Debug Log : END]')
    return (proxyMeta['ipPort'])
def source2(debug, type):
    page = (requests.get('https://www.proxy-list.download/api/v1/get?type='+type, proxies=proxies, timeout=10))
    soup = (BeautifulSoup(page.text, 'html.parser').text)
    if (debug==1):
        print('         [Source 2 : Soteria Debug Log : START]')
        print('     [TYPE]      '+type)
        print('     [COUNT]     '+str(len(soup.splitlines())))
        print('         [Source 2 : Soteria Debug Log : END]')
    return (soup)
def source3(debug):
    page = (requests.get('https://api.getproxylist.com/proxy', timeout=10))
    soup = (BeautifulSoup(page.text, 'html.parser').text)
    proxyData = (json.loads(soup))
    if "error" in proxyData:
        return ''
    if (debug==1):
        print('         [Source 3 : Soteria Debug Log : START]')
        print('     [IP:PORT]   '+proxyData['ip']+':'+str(proxyData['port']))
        print('     [TYPE]      '+proxyData['protocol'])
        print('     [COUNTRY]   '+proxyData['country'])
        print('     [CHECKED]   '+proxyData['lastTested'])
        print('     [LEVEL]     '+proxyData['anonymity'])
        print('     [HTTPS]     '+str(proxyData['allowsHttps']))
        print('     [PING]      '+proxyData['secondsToFirstByte'])
        print('         [Source 3 : Soteria Debug Log : END]')
    return (proxyData['ip']+':'+str(proxyData['port']))
try:
    sourceOne = source1(1)
    if sourceOne == '':
        proxy1 = ('')
    else:
        proxy1 = (sourceOne.split(":"))
        print(proxy1)
    if mass == True:
        self = "john"
        proxyHttp = source2(1, 'http').split("\r\n")
        for proxy in proxyHttp:
            try:
                proxyHTTPMeta = proxy.split(":")
                add(self, proxyHTTPMeta[0], proxyHTTPMeta[1], 'http')
            except Exception:
                break
        proxyHttps = source2(1, 'https').split("\r\n")
        for proxy in proxyHttps:
            try:
                proxyHTTPSMeta = proxy.split(":")
                add(self, proxyHTTPSMeta[0], proxyHTTPSMeta[1], 'https')
            except Exception:
                break
        proxySocks4 = source2(1, 'socks4').split("\r\n")
        for proxy in proxySocks4:
            try:
                proxySOCKS4Meta = proxy.split(":")
                add(self, proxySOCKS4Meta[0], proxySOCKS4Meta[1], 'socks4')
            except Exception:
                break
        proxySocks5 = source2(1, 'socks5').split("\r\n")
        for proxy in proxySocks5:
            try:
                proxySOCKS5Meta = proxy.split(":")
                add(self, proxySOCKS5Meta[0], proxySOCKS5Meta[1], 'socks5')
            except Exception:
                break
    sourceThree = source3(1)
    if sourceThree == '':
        proxy2 = ('')
    else:
        proxy2 = (sourceThree.split(":"))
        print(proxy2)
except Exception as e:
    print(e)
