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
        assert ('temp' in root['clothes'])
        clothes = listize(root['clothes']['temp'])
    data = {}
    for c in clothes:
        data[c['@value']] = {}
        for r in c['item']:
            if (not data[c["@value"]].get(r["@rain"])):
                data[c["@value"]][r["@rain"]] = {}
            if (not data[c["@value"]][r["@rain"]].get(r["@wind"])):
                data[c["@value"]][r["@rain"]][r["@wind"]] = {}
            data[c["@value"]][r["@rain"]][r["@wind"]] = r["@items"]
    return data