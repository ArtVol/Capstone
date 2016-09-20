__author__ = 'Alex'
import Tkinter as tk
from advisor import voice
import time
import data_getter


def say():
    v = voice.Voice()
    text = v.sirena(data_getter.get_weather_data_for_speech())
    v.speak(text)
    time.sleep(10)


def key_press(event):
    say()
    print('say', time.clock())

root = tk.Tk()
root.bind('<KeyPress>', key_press)
root.mainloop()