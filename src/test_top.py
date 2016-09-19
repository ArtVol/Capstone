from os import remove
import pprint
__author__ = 'Alex'
from renders import render
from urllib2 import URLError
from requests import ConnectionError
from requester import asker
from advisor import voice
from settings import settings_reader
import time

def get_weather(coords):
    try:
        weather_data_for_index = asker.get_weather_by_coords(lat=coords['lat'],
                                                             lon=coords['lon'],
                                                             current=False)
        weather_data_for_speech = asker.get_weather_by_coords(lat=coords['lat'],
                                                              lon=coords['lon'])

        return weather_data_for_index, weather_data_for_speech
    except URLError:
        print("Sorry, master. Can not get URL.")
    except ConnectionError:
        print("Sorry, master. No internet connection.")

    return None, None

v = voice.Voice()
while(True):
    coords = settings_reader.get_coords()
    weather_data_for_index, weather_data_for_speech = get_weather(coords)
    text = v.sirena(weather_data_for_speech)
    render.get_index(weather_data_for_index, text)
    # v.speak(text)
    #time.sleep(40)
    print 'Iter'
    exit()
