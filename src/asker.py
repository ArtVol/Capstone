__author__ = 'Alex'

import urllib2
import pprint
import json
"""
Parameters:
    code Internal parameter
    message Internal parameter
    city
        city.id City ID
        city.name City name
        city.coord
            city.coord.lat City geo location, latitude
            city.coord.lon City geo location, longitude
        city.country Country code (GB, JP etc.)
    cnt Number of lines returned by this API call
    list
        list.dt Time of data forecasted, unix, UTC
        list.main
            list.main.temp Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
            list.main.temp_min Minimum temperature at the moment of calculation. This is deviation from 'temp' that is possible for large cities and megalopolises geographically expanded (use these parameter optionally). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
            list.main.temp_max Maximum temperature at the moment of calculation. This is deviation from 'temp' that is possible for large cities and megalopolises geographically expanded (use these parameter optionally). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
            list.main.pressure Atmospheric pressure on the sea level by default, hPa
            list.main.sea_level Atmospheric pressure on the sea level, hPa
            list.main.grnd_level Atmospheric pressure on the ground level, hPa
            list.main.humidity Humidity, %
            list.main.temp_kf Internal parameter
        list.weather (more info Weather condition codes)
            list.weather.id Weather condition id
            list.weather.main Group of weather parameters (Rain, Snow, Extreme etc.)
            list.weather.description Weather condition within the group
            list.weather.icon Weather icon id
        list.clouds
            list.clouds.all Cloudiness, %
        list.wind
            list.wind.speed Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour.
            list.wind.deg Wind direction, degrees (meteorological)
        list.rain
            list.rain.3h Rain volume for last 3 hours, mm
        list.snow
            list.snow.3h Snow volume for last 3 hours
        list.dt_txt Data/time of caluclation, UTC
"""
def get_weather_by_citi(siti_name='Moscow,ru',
               resp_type='json',
               api_key='75b6261dbe3a53e99112252f5435a9cc',
               current=True): #weather forecast
    req_type = 'weather'
    if not current:
        req_type = 'forecast'
    url = 'http://api.openweathermap.org/data/2.5/{}?q={}&mode={}&appid={}&units=metric'\
        .format(req_type, '"{}"'.format(siti_name), resp_type, api_key)
    sock = urllib2.urlopen(url)
    data = json.load(sock)
    sock.close()

    return data

# 55.684647, 37.340472 Skoltech
def get_weather_by_coords(lat=55.684647,
                         lon=37.340472,
                         resp_type='json',
                         api_key='75b6261dbe3a53e99112252f5435a9cc',
                         current=True):
    req_type = 'weather'
    if not current:
        req_type = 'forecast'
    url = 'http://api.openweathermap.org/data/2.5/{}?lat={}&lon={}&mode={}&appid={' \
          '}&units=metric'\
        .format(req_type, lat, lon, resp_type, api_key)
    sock = urllib2.urlopen(url)
    data = json.load(sock)
    sock.close()

    return data