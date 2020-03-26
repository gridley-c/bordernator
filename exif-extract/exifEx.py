#! python3

from iptcinfo3 import IPTCInfo
import re

#info = IPTCInfo('img3.jpg')
#title = str(info['object name'])
#website = str(info['copyright notice'])
#author = str(info['by-line'])
#print(f"{title[1:]} | {website[2:-1]} | {author[2:-1]}")
#label = (f"{title[1:]} | {website[2:-1]} | {author[2:-1]}")
#print(label)


def label_extract(file):
    info = IPTCInfo(file)
    title = str(info['object name'])
    website = str(info['copyright notice'])
    author = str(info['by-line'])
    label = (f"{title[1:]} | {website[2:-1]} | {author[2:-1]}")
    print(label)

file = 'img3.jpg'
label_extract(file)
