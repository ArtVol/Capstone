__author__ = 'Alex'
import re
from playsound import playsound
import os


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

if 'file.say' in os.listdir(os.path.curdir):
    os.remove('file.say')