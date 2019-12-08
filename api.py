#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps, loads, dumps
from re import search
from random import randint
db_connect = create_engine('sqlite:///proxies.db')
app = Flask(__name__)
api = Api(app)
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
        query = conn.execute("select * from proxies where type = 'socks4';")
        proxiesMeta = (dumps(query.cursor.fetchall()))
        luckyNumber = randint(0, len(loads(proxiesMeta)))
        return (loads(proxiesMeta)[luckyNumber])
api.add_resource(http, '/http')
api.add_resource(https, '/https')
api.add_resource(socks4, '/socks4')
api.add_resource(socks5, '/socks5')
if __name__ == '__main__':
     app.run()