import pprint
from urllib2 import URLError
from requests import ConnectionError

from voice import Voice
from asker import get_weather_by_citi
from asker import get_weather_by_coords

v = Voice()
#data = get_wather_by_coords(current=True)
try:
    data = get_weather_by_citi()
    v.jarvis(data)
except URLError:
    print("Sorry, master. Can not get URL.")
except ConnectionError:
    print("Sorry, master. No internet connection.")

