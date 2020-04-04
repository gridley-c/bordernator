from PIL import Image
from PIL.ExifTags import TAGS

def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    #return(ret)
    artist = (ret['Artist'])
    copy = (ret['Copyright'])
    print(f"{artist}{copy}")
    
get_exif('fuj5.jpg')
