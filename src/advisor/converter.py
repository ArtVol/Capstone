#!/usr/bin/env python3
import pprint
from math import fabs

class Converter():
    def getIndex(self, data, value):
        a = 0
        dif = 100
        val = map(int, data.keys())
        for item in val:
            if dif >= fabs(item - value):
                dif = fabs(item - value)
                a = item
        return a

    def conv(self, parse, data):
        weather = {}

        # RAIN
        if "drizzle" in data['weather'][0]['description'] or "light rain" in data['weather'][0]['description']:
            weather["RAIN"] = "light rain"
        elif "rain" in data['weather'][0]['description']:
            weather["RAIN"] = "strong rain"
        else:
            weather["RAIN"] = "no"

        # WIND
        if data["wind"]["speed"] < 5:
            weather["WIND"] = "no"
        else:
            weather["WIND"] = "yes"

        # TEMP
        weather["TEMP"] = (int(data["main"]["temp"]))

        return weather