__author__ = 'Alex'
import os
import Tkinter as tk
from advisor import weather
from advisor import voice
from requester import asker
import time


def say():
    v = voice.Voice()
    data = asker.get_weather_by_coords(current=False)['list']
    text = v.sirena(weather.get_today_weather(data), voice=True)
    filename = 'audio{}.mp3'.format(time.strftime("%Y-%m-%d_%H_%M_%S"))
    v.speak(text, filename)
    time.sleep(10)
    os.system("rm {}".format(filename))

def key_press(event):
    say()
    print 'say', time.strftime("%Y-%m-%d %H:%M:%S")

root = tk.Tk()
root.bind('<KeyPress>', key_press)
root.mainloop()