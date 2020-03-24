#! python3
# Bordenator will apply a border and text label of the same relative size to any resolution image files found in the same directory


from glob import glob
from PIL import Image, ImageOps, ImageDraw, ImageFont

file_list = glob('*.JPG')


print("I found these files:")
print(file_list)


print("What colour do you want the border?")
border_colour = None
while border_colour not in {"black", "white"}:
    border_colour = input("Please choose black or white: ")

for photo in file_list:
    im=Image.open(photo)
    im.size
    photo_x = im.size[0]
    photo_y = im.size[1]
    font_size = int(0.005 * (max(photo_x, photo_y)))
    txt_x = (int(0.005 * photo_x))
    txt_y = (int(0.005 * photo_y))

    if (photo_x / photo_y) >= 1.6: 
        border_y_px = int(0.1 * photo_y)
        border_photo = ImageOps.expand(im, border=(1, border_y_px), fill=(border_colour))
        font = ImageFont.truetype("Symtext.ttf", font_size)
        signed = ImageDraw.Draw(border_photo)
        signed.text((txt_x,txt_y), "DERELICTE WORLD | CARL GRIDLEY", font = font, fill=(125,125,125))
        border_photo.save('bordered-%s' %photo, quality=94)
    
    else:
        border_px = int(0.03 * max(photo_x, photo_y))
        border_photo = ImageOps.expand(im, border=border_px, fill=(border_colour)) 
        font = ImageFont.truetype("Symtext.ttf", font_size)
        signed = ImageDraw.Draw(border_photo)
        signed.text((txt_x,txt_y), "DERELICTE WORLD | CARL GRIDLEY", font = font, fill=(125,125,125))
        border_photo.save('bordered-%s' %photo, quality=94)

