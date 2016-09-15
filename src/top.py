from urllib2 import URLError

from requests import ConnectionError

from requester import asker
from advisor import voice

v = voice.Voice()
#data = get_wather_by_coords(current=True)
try:
    data = asker.get_weather_by_citi()
    v.jarvis(data)
except URLError:
    print("Sorry, master. Can not get URL.")
except ConnectionError:
    print("Sorry, master. No internet connection.")

