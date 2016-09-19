import pprint
from urllib2 import URLError

from requests import ConnectionError

from requester import asker
from advisor import voice
from advisor import weather

v = voice.Voice()
try:
    data = weather.get_today_weather()
    text = v.sirena(data)
    print text
    # v.speak(text)
except URLError:
    print("Sorry, master. Can not get URL.")
except ConnectionError:
    print("Sorry, master. No internet connection.")

