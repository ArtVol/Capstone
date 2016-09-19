#!/usr/bin/env python3
import os

import sys
import xmltodict

def listize(obj):
    return obj if isinstance(obj, list) else [obj]

# XML clothes parser
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
        outerwear = listize(root['clothes']['thing']['outerwear']['item'])
    data = {
         "HEAD":    {},
         "OUTERWEAR": {},
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
    for c in outerwear:
        data["OUTERWEAR"][c["@name"]] = {
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
        xmls_dir = os.path.join('advisor','xmls','new_clothes.xml')
        with open(xmls_dir) as src:
            parse = doParse(src)
        out = ''
        for p in parse:
            for c in parse[p]:
                if data["RAIN"] in parse[p][c]["RAIN"]:
                    if data["WIND"] in parse[p][c]["WIND"] or "all" in parse[p][c]["WIND"]:
                        if data["TEMP"] >= int(parse[p][c]["TEMP"][0]) and data["TEMP"] <= int(parse[p][c]["TEMP"][1]):
                            out += c + ", "
        return out