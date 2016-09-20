import os
import pprint
import sys
from mako.template import Template

def q_compare(value1, value2):
    comp1, comp2 = int(round(value1)), int(round(value2))

    if comp1 != comp2:
        return str(comp1) + ' ~ ' + str(comp2)

    return comp2


def get_title(time1, time2):
    table = {'00--03': 'Night',
             '03--06': 'Night',
             '06--09': 'Morning',
             '09--12': 'Morning',
             '12--15': 'Day',
             '15--18': 'Day',
             '18--21': 'Evening',
             '21--00': 'Evening'}

    # 2016-09-13 15:00:00
    return table[time1[11:13] + '--' + time2[11:13]]

def hpa2torr(value):
    return value * 0.75006375541921

def plot_pair_data(r_data):
    pair_data = [{}]*len(r_data)
    for i in xrange(len(r_data)):
        first, second = r_data[i]
        pair_data[i] = {'icon':     second['weather'][0]['icon'],
                        'temp':     q_compare(first['main']['temp'],
                                              second['main']['temp']),
                        'clouds':   q_compare(first['clouds']['all'],
                                              second['clouds']['all']),
                        'humidity': q_compare(first['main']['humidity'],
                                              second['main']['humidity']),
                        'wind':     q_compare(first['wind']['speed'],
                                              second['wind']['speed']),
                        'pressure': q_compare(hpa2torr(first['main']['pressure']),
                                              hpa2torr(second['main']['pressure'])),
                        'title':    get_title(first['dt_txt'],
                                              second['dt_txt'])}

    return pair_data


def get_time_weather(data):# data = asker.get_weather_by_coords(current=False)
    w_list = data['list'][0:8]
    r_data = [(w_list[i], w_list[i + 1]) for i in xrange(0, len(w_list) - 1, 2)]
    parts = plot_pair_data(r_data)

    return parts

def _write2pattern(template_name, file_name, data):
    with open(file_name, "w") as f:
        f.write((Template(filename=template_name).render_unicode(**data)))


def get_index(r_data,
              cur_data,
              speech_text,
              src_path=os.path.join('renders', 'templates'),
              dst_path='html'):
    weather = get_time_weather(r_data)
    cur_w = {'icon':     cur_data['weather'][0]['icon'],
             'temp':     cur_data['main']['temp'],
             'clouds':   cur_data['clouds']['all'],
             'humidity': cur_data['main']['humidity'],
             'wind':     cur_data['wind']['speed'],
             'pressure': round(hpa2torr(cur_data['main']['pressure']), 2),
             'title':    'Now'}

    for i, w in zip(xrange(len(weather)), weather):
        dst_file_name = os.path.join(dst_path, 'fill{}.html'.format(i))
        src_file_name = os.path.join(src_path, 'fill')
        _write2pattern(src_file_name, dst_file_name, {'value': w})

    dst_file_name = os.path.join(dst_path, 'report.html')
    src_file_name = os.path.join(src_path, 'report')
    _write2pattern(src_file_name, dst_file_name, {'speech': speech_text})
