#!/usr/bin/env python3
import os

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
        assert ('item' in root['clothes']['thing']['head'])
        assert ('item' in root['clothes']['thing']['top'])
        assert ('item' in root['clothes']['thing']['pants'])
        assert ('item' in root['clothes']['thing']['shoes'])
        assert ('item' in root['clothes']['thing']['other'])
        # top = listize(root['clothes']['thing'])
        head= listize(root['clothes']['thing']['head']['item'])
        top = listize(root['clothes']['thing']['top']['item'])
        pants = listize(root['clothes']['thing']['pants']['item'])
        shoes = listize(root['clothes']['thing']['shoes']['item'])
        other = listize(root['clothes']['thing']['other']['item'])
    data = {
         "HEAD":    {},
         "TOP":     {},
         "PANTS":   {},
         "SHOES":   {},
         "OTHER":  {}
    }
    for c in head:
        data["HEAD"][c["@name"]] = {
             "SIZE":    c['size'],
             "TEMP":    c['temp'].split("/"),
             "WIND":    c['wind'],
             "RAIN":    c['rain'],
             "SEASON":  c['season']
        }
    for c in top:
        data["TOP"][c["@name"]] = {
             "SIZE":    c['size'],
             "TEMP":    c['temp'].split("/"),
             "WIND":    c['wind'],
             "RAIN":    c['rain'],
             "SEASON":  c['season']
        }
    for c in pants:
        data["PANTS"][c["@name"]] = {
             "SIZE":    c['size'],
             "TEMP":    c['temp'].split("/"),
             "WIND":    c['wind'],
             "RAIN":    c['rain'],
             "SEASON":  c['season']
        }
    for c in shoes:
        data["SHOES"][c["@name"]] = {
             "SIZE":    c['size'],
             "TEMP":    c['temp'].split("/"),
             "WIND":    c['wind'],
             "RAIN":    c['rain'],
             "SEASON":  c['season']
        }
    for c in other:
        data["OTHER"][c["@name"]] = {
             "SIZE":    c['size'],
             "TEMP":    c['temp'].split("/"),
             "WIND":    c['wind'],
             "RAIN":    c['rain'],
             "SEASON":  c['season']
        }
    return data

def clothesAdvisor(data):
        parse = {}
        xmls_dir = os.path.abspath('advisor\\xmls')
        with open(xmls_dir + "\\new_clothes.xml") as src:
            parse = doParse(src)
        out = ''
        print data
        for p in parse:
            for c in parse[p]:
                print c, parse[p][c]["TEMP"][0], parse[p][c]["TEMP"][1]
                if data["RAIN"] in parse[p][c]["RAIN"]:
                    if data["WIND"] in parse[p][c]["WIND"]:
                        if data["TEMP"] >= int(parse[p][c]["TEMP"][0]) and data["TEMP"] <= int(parse[p][c]["TEMP"][1]):
                            print data["TEMP"] <= parse[p][c]["TEMP"][1], data["TEMP"], parse[p][c]["TEMP"][0], parse[p][c]["TEMP"][1]
                            print
                            out += c + ", "
        return out