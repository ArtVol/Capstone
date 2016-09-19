from os import remove
__author__ = 'Alex'
from renders import render
from urllib2 import URLError
from requests import ConnectionError
from requester import asker
from advisor import voice
import time

def get_weather():
    try:
        weather_data_for_index = asker.get_weather_by_coords(current=False)
        weather_data_for_speech = asker.get_weather_by_coords()

        return weather_data_for_index, weather_data_for_speech
    except URLError:
        print("Sorry, master. Can not get URL.")
    except ConnectionError:
        print("Sorry, master. No internet connection.")

    return None, None

v = voice.Voice()
while(True):
    weather_data_for_index, weather_data_for_speech = get_weather()
    text = v.sirena(weather_data_for_speech)
    render.get_index(weather_data_for_index, text)
    # v.speak(text)
    time.sleep(40)
    print 'Iter'
