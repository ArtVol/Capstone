__author__ = 'Alex'
import os
import re

def get_coords(file_sett=os.path.join('settings', 'setting')):
    sett = get_settings(file_sett)['location']
    # location: lat=55.684647, lon=37.340472;
    lat = float(re.findall(r'lat=(\d+(?:\.?\d+))', sett)[0])
    lon = float(re.findall(r'lon=(\d+(?:\.?\d+))', sett)[0])

    return {'lat': lat, 'lon': lon}

def get_settings(file_sett=os.path.join('settings', 'setting')):
    with open(file_sett) as f:
        r_str_data = f.read()
    r_data = {i.split(':')[0]: i.split(':')[1]
              for i in re.sub(r'\s*', '', r_str_data).split(';')
              if i}

    return r_data