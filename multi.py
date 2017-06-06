'''
This script takes a jpg image and creates multiple copies. Each of which
has a watermark that is not visible to the naked eye. The watermark on 
each of the images is shifted slightly in location from the previous image.
This makes each image optically unique as well as produce a different has value

'''
import os
import sys
from PIL import Image, ImageDraw, ImageFont
# finding a file in the current directory that is a jpeg
FILES = os.listdir('.')
for index, item in enumerate(FILES):
    if ".jpg" in item:
        img_location = index

AMOUNT = int(input("How many copies would you like?\nEnter number: "))
# Setting up progress bar
TOOLBAR_WIDTH = 50
sys.stdout.write("Copy Progress: [%s]" % (" " * TOOLBAR_WIDTH))
sys.stdout.flush()
sys.stdout.write("\b" * (TOOLBAR_WIDTH+1))
# setting up all variables

# AMOUNT = 500

# selecting the file that is a jpeg amoung other FILES
IMG_FILE = FILES[img_location]
# Getting the last occurrence of the period to get file EXTENSION
LAST_DOT = IMG_FILE.rfind('.')
# Splitting the file into file name and EXTENSION name
NAME = IMG_FILE[:LAST_DOT]
EXTENSION = IMG_FILE[LAST_DOT+1:]
# opens image file
BASE = Image.open(IMG_FILE).convert('RGBA')


def multi_watermark(amount, base_image, txt='SaveMyServer'):
    '''
    Takes an image and makes multiple copies with a watermark
    '''
    # get a font
    fnt = ImageFont.truetype('arial.ttf', 60)
    # sets OPACITY of the water mark
    opacity = 1
    # this is the predicted width of the water mork text
    text_width = 400
    # The increment the watermark is moved for each image
    step = (base_image.size[0] - text_width) / amount
    position = 0
    # Loop to make multiple images
    for i in xrange(amount):
        position += step
        txt = Image.new('RGBA', base_image.size, (255, 255, 255, 0))
        d = ImageDraw.Draw(txt)
        d.text((position, 10), "SaveMyServer", font=fnt, fill=(0, 0, 0, opacity))
        out = Image.alpha_composite(base_image, txt)
        out.save(NAME + "-watermarked-" + str(i + 1)+ "." + EXTENSION)

if __name__ == '__main__':
    multi_watermark(AMOUNT, BASE)
