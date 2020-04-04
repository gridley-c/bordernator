#! python3

#logic for extracting the label to be used from the IPTC metadata, if the user wants it
#IPTCInfo doesn't return a dictionary as far as I can tell, so we need to convert to a string to check if a label exists

from iptcinfo3 import IPTCInfo
import re

def label_extract(photo):
    info = IPTCInfo(photo)
    str_info = str(info)
    infoRegex = re.compile(r'\'(\w.*\w)\'')
    
    if 'object name' in str_info:
        titleRaw = str(info['object name'])
        mot = infoRegex.search(titleRaw)
        if mot is None:
            title = ""
        else:
            title = (f"\'{mot.group(1)}\'")

    else:
        title = ""       

    if 'copyright notice' in str_info:
        websiteRaw = str(info['copyright notice'])
        mow = infoRegex.search(websiteRaw)
        if mow is None:
            website = ""
        else:
            website = (f"{mow.group(1)}  ")
        
    else:
        website = ""

    if 'by-line' in str_info:
        byLineRaw = str(info['by-line'])
        mob = infoRegex.search(byLineRaw)
        if mob is None:
            author = ""
        else:
            author = (f"{mob.group(1)}  ")
        
    else:
        author = ""

    label = (f"{website}{author}{title}")
    return(label)


label = label_extract("img4.jpg")
print(label)
