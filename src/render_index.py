__author__ = 'Alex'
from renders import render
import data_getter
from advisor import voice
import time

v = voice.Voice()
while(True):
    weather_data_for_index = data_getter.get_weather_data_for_index()
    weather_data_for_speech = data_getter.get_weather_data_for_speech()
    coords = {'lat': 12, 'lon': 12}
    current_weather = data_getter.get_current_weather_data(coords)
    text = v.sirena(weather_data_for_speech)
    render.get_index(weather_data_for_index, current_weather, text)
    time.sleep(10)
    print('Iter')
