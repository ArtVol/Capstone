#!/usr/bin/env python3
import pprint
from math import fabs

class Converter():
    def getIndex(self, data, value):
        a = 0
        dif = 100
        val = map(float, data.keys())

        for item in val:
            if dif >= fabs(item - value):
                dif = fabs(item - value)
                a = item
        return a

    def day_conv(self, data):
        weather = {}

        # RAIN
        if "drizzle" in data['weather'][0]['description'] or "light" in data['weather'][0]['description']:
            weather["RAIN"] = "light rain"
        elif "rain" in data['weather'][0]['description']:
            weather["RAIN"] = "strong rain"
        else:
            weather["RAIN"] = "no"

        # WIND
        # Beaufort scale
        wind = {
            "0-0.3": "calm",  # 0.3 m/s
            "0.4-1.5": "light air",  # 1.5 m/s
            "1.6-3.3": "ligth breeze",  # 3.3 m/s
            "3.4-5.5": "gentle breeze",  # 5.5 m/s
            "5.6-7.9": "moderate breeze",  # 7.9 m/s
            "8-10.7": "fresh breeze",  # 10.7 m/s
            "10.8-13.8": "strong breeze",  # 13.8 m/s
            "13.9-17.1": "higth wind",  # 17.1
            "17.2-20.7": "gale",  # 20.7
            "20.8-24.4": "strong gale",  # 24.4
            "24.5-28.4": "storm",  # 28.4
            "28.5-32.6": "violent storm",  # 32.6
            "32.7-100": "hurricane force",  # more than 32.7
        }
        for w in wind:
            if float(data["wind"]["speed"]) >= float(w.split("-")[0]) and float(data["wind"]["speed"]) <= float(w.split("-")[1]):
                weather["WIND"] = wind[w]

        #
        # wind = {
        #     0.15: "calm",           # 0.3 m/s
        #     0.9: "light air",       # 1.5 m/s
        #     2.4: "ligth breeze",    # 3.3 m/s
        #     4.4: "gentle breeze",   # 5.5 m/s
        #     6.7: "moderate breeze", # 7.9 m/s
        #     9.3: "fresh breeze",   # 10.7 m/s
        #     12.25: "strong breeze",  # 13.8 m/s
        #     15.45: "higth wind",     # 17.1
        #     18.9: "gale",           # 20.7
        #     22.55: "strong gale",    # 24.4
        #     26.4: "storm",          # 28.4
        #     30.5: "violent storm",  # 32.6
        #     100: "hurricane force", # more than 32.7
        # }
        # index = self.getIndex(wind, data["wind"]["speed"])
        # weather["WIND"]  = wind[index]
        # print weather["WIND"]

        # TEMP
        weather["TEMP"] = (int(data["main"]["temp"]))

        return weather

    def conv(self, data):
        weather = {}

        # RAIN
        for item in data["RAIN"]:
            if "drizzle" in data['RAIN'][item] or "light" in data['RAIN'][item]:
                weather["RAIN"] = "light rain"
            elif "rain" in data['RAIN'][item]:
                weather["RAIN"] = "strong rain"
            else:
                weather["RAIN"] = "no"

        # WIND
        # Beaufort scale
        wind = {
            "0-0.4": "calm",  # 0.3 m/s
            "0.4-1.6": "light air",  # 1.5 m/s
            "1.6-3.4": "ligth breeze",  # 3.3 m/s
            "3.4-5.6": "gentle breeze",  # 5.5 m/s
            "5.6-8": "moderate breeze",  # 7.9 m/s
            "8-10.8": "fresh breeze",  # 10.7 m/s
            "10.8-13.9": "strong breeze",  # 13.8 m/s
            "13.9-17.2": "higth wind",  # 17.1
            "17.2-20.8": "gale",  # 20.7
            "20.8-24.5": "strong gale",  # 24.4
            "24.5-28.5": "storm",  # 28.4
            "28.5-32.7": "violent storm",  # 32.6
            "32.7-101": "hurricane force",  # more than 32.7
        }
        for w in wind:
            if float(data['WIND']['MAX']) >= float(w.split("-")[0]) and float(data["WIND"]["MAX"]) < float(w.split("-")[1]):
                weather["WIND"] = wind[w]

        # TEMP
        weather["TEMP"] = (data["TEMP"])
        return weather