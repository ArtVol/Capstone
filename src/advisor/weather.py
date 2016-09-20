import pprint
from time import strftime
from src.requester import asker

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def parser():
    window = 8
    data = asker.get_weather_by_coords(current=False)['list']
    parsed = {}

    i = 0
    for item in data:
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
    night_time = ["21:00:00","00:00:00","03:00:00"]

    iter = sorted(data)[0]
    cur_t = data[iter]["TEMP"]
    night_t = []
    day_t = []

    for item in sorted(data):
        time = item.split(" ")[1]
        if time in night_time:
            night_t.append(data[item]["TEMP"])
        else:
            day_t.append(data[item]["TEMP"])

    weather["TEMP"] = {
        "NOW"   : int(cur_t),
        "NIGHT" : int(round(mean(night_t))),
        "DAY"   : int(round(mean(day_t)))
    }

    min_wind = min(data[item]["WIND"] for item in data)
    max_wind = max(data[item]["WIND"] for item in data)
    weather["WIND"] = {
        "MIN": min_wind,
        "MAX": max_wind
    }
    weather["RAIN"] = {}
    for item in sorted(data):
        time = item
        # if "rain" in data[item]['DESCRIPTION']:
        if time > strftime("%Y-%m-%d %H:%M:%S"):
            if not data[item]['DESCRIPTION'] in weather["RAIN"].values():
                weather["RAIN"][time] = data[item]['DESCRIPTION']

    return weather