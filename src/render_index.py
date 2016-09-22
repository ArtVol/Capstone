__author__ = 'Alex'
import webbrowser
import os
from renders import render
import data_getter
from advisor import voice
from advisor import weather
from requester import asker
import time

def render_ind():
    v = voice.Voice()
    #while(True):
    weather_data_for_index = data_getter.get_weather_data_for_index()
    coords = {'lat': 55.75, 'lon': 37.62} # Moscow coords
    current_weather = data_getter.get_current_weather_data(coords)
    data = asker.get_weather_by_coords(current=False)['list']
    weather_data_for_speech = weather.get_today_weather(data)
    weather_text = v.get_html_weather_text(weather_data_for_speech)
    clothes_text = v.get_clothes_text(weather_data_for_speech)
    render.get_index(weather_data_for_index, current_weather, weather_text, clothes_text)
    print('Iter')
    # time.sleep(360)
