__author__ = 'Alex'

import re
from playsound import playsound
import os


def say():
    file_name = ''
    for f in os.listdir(os.path.curdir):
        if re.search(r'.*\.mp3', f):
            file_name = f
            break
    if file_name:
        playsound(file_name)
        print 'Say weather'
    else:
        print 'No any mp3'


def find_file():
    return 'file.say' in os.listdir(os.path.curdir)

while(True):
    if find_file():
        say()
        os.remove('file.say')