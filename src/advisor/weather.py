import pprint
from time import strftime

from src.requester import asker

def parser():
    window = 8
    data = asker.get_weather_by_coords(current=False)['list']
    parsed = {}

    ctime = strftime("%Y-%m-%d")
    i = 0
    for item in data:
        day  = item['dt_txt'].split(" ")[0]
        time = item['dt_txt']

        if i < window:
            if not parsed.get(time):
                parsed[time] = {}
            parsed[time]['DESCRIPTION'] = item["weather"][0]['description']
            parsed[time]['TEMP'] = item["main"]['temp']
            parsed[time]['WIND'] = item["wind"]['speed']
        i += 1

    return parsed

def get_today_weather():
    data = parser()

    weather = {}
    min_tmp = min(data[item]["TEMP"] for item in data)
    max_tmp = max(data[item]["TEMP"] for item in data)
    weather["TEMP"] = {
        "MIN" : int(min_tmp),
        "MAX" : int(max_tmp)
    }
    weather["WIND"] = {
        "MIN": min(data[item]["WIND"] for item in data),
        "MAX": max(data[item]["WIND"] for item in data)
    }
    weather["RAIN"] = {}
    for item in sorted(data):
        time = item
        # if "rain" in data[item]['DESCRIPTION']:
        if not data[item]['DESCRIPTION'] in weather["RAIN"].values():
            weather["RAIN"][time] = data[item]['DESCRIPTION']

    return weather