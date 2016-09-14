__author__ = 'Alex'
from renders import render
from requester import asker

data = asker.get_weather_by_coords(current=False)
render.get_index(data)