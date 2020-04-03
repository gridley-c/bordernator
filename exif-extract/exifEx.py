#! python3

#logic for extracting the label to be used from the IPTC metadata, if the user wants it
#IPTCInfo doesn't return a dictionary as far as I can tell, so we need to convert to a string to check if a label exists

from iptcinfo3 import IPTCInfo

def label_extract(photo):
    info = IPTCInfo(photo)
    str_info = str(info)
    
    if 'object name' in str_info:
        title = str(info['object name'])
    else:
        title = ""
    
    if 'copyright notice' in str_info:
        website = str(info['copyright notice'])
    else:
        website = ""

    if 'by-line' in str_info:
        author = str(info['by-line'])
    else:
        author = ""
    
    label = (f"{author[2:-1]} | {website[2:-1]} | {title[1:]}")
    return(label)


label = label_extract("img3.jpg")
print(label)
