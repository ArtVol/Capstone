__author__ = 'Alex'
from renders import render
import data_getter
from advisor import voice
from settings import settings_reader
import time

v = voice.Voice()
while(True):
    weather_data_for_index = data_getter.get_weather_data_for_index()
    weather_data_for_speech = data_getter.get_weather_data_for_speech()
    current_weather = data_getter.get_current_weather_data()
    text = v.sirena(weather_data_for_speech)
    render.get_index(weather_data_for_index, current_weather, text)
    time.sleep(10)
    print 'Iter'
