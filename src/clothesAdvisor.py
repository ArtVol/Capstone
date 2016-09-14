import pprint

from re import search

from converter import Converter

#!/usr/bin/env python3
import xmltodict

def listize(obj):
    return obj if isinstance(obj, list) else [obj]

def doParse(src):
    # Read from XML
    root = xmltodict.parse(src)
    if 'clothes' in root:
        clothes = None
        # print root['clothes']['temp'][1]['rain']
        assert ('thing' in root['clothes'])
        assert ('top' in root['clothes']['thing'])
        assert ('item' in root['clothes']['thing']['top'])
        # top = listize(root['clothes']['thing']['top']['item'])
        top = listize(root['clothes']['thing'])
        pants = listize(root['clothes']['thing']['pants']['item'])
    # data = {
    #     "HEAD":    {},
    #     "OUTWEAR": {},
    #     "TOP":     {},
    #     "PANTS":   {},
    #     "SHOES":   {}
    # }
    data = {}
    for a in top[0]:
        for b in top[0][a]:
            oneType = top[0][a][b]
            print oneType
            if(not data.get(a.upper())):
                data[a.upper()] = {}
            for c in oneType:
                data[a.upper()][c["@name"]] = {
                    "SIZE":   c['size'],
                    "TEMP":   c['temp'].split("/"),
                    "WIND":   c['wind'],
                    "RAIN":   c['rain'],
                    "SEASON": c['season']
                }
    # for c in top:
    #     data["TOP"][c["@name"]] = {
    #         "SIZE":    c['size'],
    #         "TEMP":    c['temp'].split("-"),
    #         "WIND":    c['wind'],
    #         "RAIN":    c['rain'],
    #         "SEASON":  c['season']
    #     }
    # for c in pants:
    #     data["PANTS"][c["@name"]] = {
    #         "SIZE":   c['size'],
    #         "TEMP":   c['temp'].split("-"),
    #         "WIND":   c['wind'],
    #         "RAIN":   c['rain'],
    #         "SEASON": c['season']
    #     }
    return data

def clothesAdvisor(data):
        parse = {}
        with open("new_clothes.xml") as src:
            parse = doParse(src)
        out = ''
        for p in parse:
            for c in parse[p]:
                if data["RAIN"] in parse[p][c]["RAIN"]:
                    if data["WIND"] in parse[p][c]["WIND"]:
                        if data["TEMP"] >= parse[p][c]["TEMP"][0] and data["TEMP"] <= parse[p][c]["TEMP"][1]:
                            out += c + ", "
        return out