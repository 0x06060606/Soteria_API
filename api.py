#!/usr/bin/python3
import json, requests, socket, urllib3, os, random
from flask import Flask, request, jsonify, render_template, Markup, send_from_directory
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps, loads, dumps
from re import search
from random import randint
from threading import Thread
from time import time
db_connect = create_engine('sqlite:///proxies.db')
app = Flask(__name__, template_folder='./html')
api = Api(app)
@app.route('/')
def index():
    return render_template('home.html')
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
def check(proxy, proxType, url):
    try:
        requests.get(url,proxies={''+proxType:proxType+'://'+proxy},timeout=(3.05,27))
        return True
    except Exception:
        return False
def getProxy(proxType):
    headers = {'Content-Type': 'application/json', 'Authorization': '{0}'.format('null')}
    api_url = '{0}{1}'.format("https://proxy.soteria.cf/", proxType)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
class null(Resource):
    def get(self):
        return ('bruh')
class http(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from proxies where type = 'http';")
        proxiesMeta = (dumps(query.cursor.fetchall()))
        luckyNumber = randint(0, len(loads(proxiesMeta)))
        return (loads(proxiesMeta)[luckyNumber])
class https(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from proxies where type = 'https';")
        proxiesMeta = (dumps(query.cursor.fetchall()))
        luckyNumber = randint(0, len(loads(proxiesMeta)))
        return (loads(proxiesMeta)[luckyNumber])
class socks4(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from proxies where type = 'socks4';")
        proxiesMeta = (dumps(query.cursor.fetchall()))
        luckyNumber = randint(0, len(loads(proxiesMeta)))
        return (loads(proxiesMeta)[luckyNumber])
class socks5(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from proxies where type = 'socks5';")
        proxiesMeta = (dumps(query.cursor.fetchall()))
        luckyNumber = randint(0, len(loads(proxiesMeta)))
        return (loads(proxiesMeta)[luckyNumber])
def pacMeta()
    n=(10)
    proxyVan=("")
    while n > 0:
        proxyMeta=(getProxy('http'))
        proxy=proxyMeta[0]+":"+proxyMeta[1]
        if (check(proxy,'http',"http://www.google.com/")==True):
            n-=1
            proxyBus=("PROXY "+proxyBus+proxy+"; ")
        else:
            n+=1
        proxyVan=(proxyVan+proxyBus)
    return (proxyVan)
@app.route('/soteria.pac')
def pac():
    return ('function FindProxyForURL(url, host){ return "'+pacMeta()+'" }')
api.add_resource(null, '/favicon.ico')
api.add_resource(http, '/http')
api.add_resource(https, '/https')
api.add_resource(socks4, '/socks4')
api.add_resource(socks5, '/socks5')
if __name__ == '__main__':
     app.run(host='0.0.0.0')
