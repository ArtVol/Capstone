import pprint
__author__ = 'Alex'
import re
import os
from renders import render
import data_getter
from advisor import voice
from advisor import weather
import time

def save_mp3(v, data):
    filename = 'audio{}.mp3'.format(time.strftime("%Y-%m-%d_%H_%M_%S"))
    v.save_speech(data, filename)

def check_weather_data(data):
    error_cods = ['404']
    if 'cod' in data and data['cod'] in error_cods:
        print data['cod']
        print data['message']

        return False
    return True

def remove_mp3():
    for f in os.listdir(os.path.curdir):
        if re.search(r'.*\.mp3', f):
            os.remove(f)


def render_ind():
    # coords = {'lat': 55.75,'lon': 37.62} # Moscow coords
    v = voice.Voice()

    print 'Call API'
    weather_data = data_getter.get_weather_data_for_index()
    if not check_weather_data(weather_data):
        return
    current_weather = data_getter.get_current_weather_data()
    if not check_weather_data(current_weather):
        return
    print 'API response success'

    print 'Render html start'
    weather_data_for_speech = weather.get_today_weather(weather_data['list'])

    text = v.get_html_text(weather_data_for_speech)
    render.get_index(weather_data, current_weather, text)
    print 'Render done'

    print 'Render mp3 start'
    remove_mp3()
    save_mp3(v, v.get_voice_text(weather_data_for_speech))
    print 'Success'
render_ind()