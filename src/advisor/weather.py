import pprint
from time import strftime

from src.requester import asker

def parser():
    data = asker.get_weather_by_coords(current=False)['list']
    parsed = {}
    ctime = strftime("%Y-%m-%d")
    for item in data:
        day  = item['dt_txt'].split(" ")[0]
        time = item['dt_txt'].split(" ")[1]

        if ctime == day:
            if not parsed.get(time):
                parsed[time] = {}
            parsed[time]['DESCRIPTION'] = item["weather"][0]['description']
            parsed[time]['TEMP'] = item["main"]['temp']
            parsed[time]['WIND'] = item["wind"]['speed']

    pprint.pprint(parsed)

        # pprint.pprint(item['dt_txt'])



def get_today_weather():
    data = asker.get_weather_by_citi(current=False)

parser()