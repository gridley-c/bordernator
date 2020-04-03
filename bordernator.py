#! python3
# Bordernator will apply a border and text label of the same relative size to any resolution image files found in the same directory


from glob import glob
from PIL import Image, ImageOps, ImageDraw, ImageFont
from PIL.ExifTags import TAGS
from iptcinfo3 import IPTCInfo
from pathlib import Path
import logging
import re

#there is a noisy warning from IPTCInfo that does not affect functionality, so we will suppress that
iptcinfo_logger = logging.getLogger('iptcinfo')
iptcinfo_logger.setLevel(logging.ERROR)


#gather a list of the files to be bordernated
file_list = glob('*.JPG')
file_list.extend(glob('*.jpg'))
print("I found these files:")
print(*file_list, sep = "\n")
print("\n")


#what colour do we want the border to be?
print("What colour do you want the border?")
border_colour = None
while border_colour not in {"black", "white"}:
    border_colour = input("Please choose black or white: ")
    print("\n")


#do you want a text label?
print("Do you want a text label using IPTC metadata?")
label_wanted = None
while label_wanted not in {"yes", "y", "no", "n"}:
    label_wanted = input("Please choose (y)es or (n)o: ")
    print("\n")


#logic for extracting the label to be used from the IPTC metadata, if the user wants it
#IPTCInfo doesn't seem to return a dictionary so we have to check if the tag we want exists using a string, or it will return nonsense
#I also need a regular expression to sensibly extract the text from the tags
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

    if label_wanted in {"yes", "y"}: 
       label = (f"{website}{author}{title}")
       return(label)

    else:
        label = ""
        return(label)

#logic for adding cinematic borders
def cinematicBorder(photo):
    border_y_px = int(0.1 * photo_y)
    border_photo = ImageOps.expand(im, border=(1, border_y_px), fill=(border_colour))
    font = ImageFont.truetype("Symtext.ttf", font_size)
    signed = ImageDraw.Draw(border_photo)
    signed.text((txt_x,txt_y), label_text, font = font, fill=(125,125,125))
    save_path = save_folder / (f"{border_colour}-{photo}")
    border_photo.save(save_path, quality=94, exif=exif)
    print(f"{photo} has been bordernated.")

#logic for normal borders
def squareBorder(photo):
    border_px = int(0.03 * max(photo_x, photo_y))
    border_photo = ImageOps.expand(im, border=border_px, fill=(border_colour)) 
    font = ImageFont.truetype("Symtext.ttf", font_size)
    signed = ImageDraw.Draw(border_photo)
    signed.text((txt_x,txt_y), label_text, font = font, fill=(125,125,125))
    save_path = save_folder / (f"{border_colour}-{photo}")
    border_photo.save(save_path, quality=94, exif=exif)
    print(f"{photo} has been bordernated.")


#main program logic, runs through the files and applies desired border to each
for photo in file_list:
    im=Image.open(photo)
    exif = im.info['exif']
    im.size
    photo_x = im.size[0]
    photo_y = im.size[1]
    font_size = int(0.005 * (max(photo_x, photo_y)))
    txt_x = (int(0.005 * photo_x))
    txt_y = (int(0.005 * photo_y))
    label_text = label_extract(photo)
    Path("bordernated/").mkdir(parents=True, exist_ok=True) 
    save_folder = Path('bordernated/')
    if (photo_x / photo_y) >= 1.6:
        cinematicBorder(photo)

    else:
        squareBorder(photo)


#thanks for bordernating
print("\n")
print("Thank you for using BORDERNATOR for all your bordernating needs.")
    
