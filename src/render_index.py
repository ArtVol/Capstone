__author__ = 'Alex'
from renders import render
import data_getter
from advisor import voice
from advisor import weather
from requester import asker
from settings import settings_reader
import time

v = voice.Voice()
while(True):
    weather_data_for_index = data_getter.get_weather_data_for_index()
    coords = {'lat': 12, 'lon': 12}
    current_weather = data_getter.get_current_weather_data(coords)
    data = asker.get_weather_by_coords(current=False)['list']
    weather_data_for_speech = weather.get_today_weather(data)
    text = v.sirena(weather_data_for_speech)
    render.get_index(weather_data_for_index, current_weather, text)
    time.sleep(10)
    print('Iter')
