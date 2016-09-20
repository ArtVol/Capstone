__author__ = 'Alex'
from urllib2 import URLError
from requests import ConnectionError
from requester import asker
from settings import settings_reader

def get_current_weather_data(coords=settings_reader.get_coords()):
    try:
        weather_data = asker.get_weather_by_coords(lat=coords['lat'],
                                                   lon=coords['lon'])
        return weather_data
    except URLError:
        print("Sorry, master. Can not get URL.")
    except ConnectionError:
        print("Sorry, master. No internet connection.")

    return None

def get_weather_data_for_index(coords=settings_reader.get_coords()):
    try:
        weather_data_for_index = asker.get_weather_by_coords(lat=coords['lat'],
                                                             lon=coords['lon'],
                                                             current=False)
        return weather_data_for_index
    except URLError:
        print("Sorry, master. Can not get URL.")
    except ConnectionError:
        print("Sorry, master. No internet connection.")

    return None

def get_weather_data_for_speech(coords=settings_reader.get_coords()):
    try:
        weather_data_for_speech = asker.get_weather_by_coords(lat=coords['lat'],
                                                              lon=coords['lon'])
        return weather_data_for_speech
    except URLError:
        print("Sorry, master. Can not get URL.")
    except ConnectionError:
        print("Sorry, master. No internet connection.")

    return None