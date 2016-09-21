import os

__author__ = 'Alex'
import Tkinter as tk
from advisor import weather
from advisor import voice
from requester import asker
import time
import data_getter


def say():
    v = voice.Voice()
    data = asker.get_weather_by_coords(current=False)['list']
    text = v.sirena(weather.get_today_weather(data))
    v.speak(text)
    time.sleep(10)


def key_press(event):
    say()

    print('say', time.strftime("%Y-%m-%d %H:%M:%S"))

root = tk.Tk()
root.bind('<KeyPress>', key_press)
root.mainloop()