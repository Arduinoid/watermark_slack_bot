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
# sets OPACITY of the water mark
OPACITY = 1
# AMOUNT = 500
# this is the predicted width of the water mork text
TEXT_WIDTH = 400
# selecting the file that is a jpeg amoung other FILES
IMG_FILE = FILES[img_location]
# Getting the last occurrence of the period to get file EXTENSION
LAST_DOT = IMG_FILE.rfind('.')
# Splitting the file into file name and EXTENSION name
NAME = IMG_FILE[:LAST_DOT]
EXTENSION = IMG_FILE[LAST_DOT+1:]
# opens image file
BASE = Image.open(IMG_FILE).convert('RGBA')
STEP = (BASE.size[0] - TEXT_WIDTH) / AMOUNT
# make a blank image for the text, initialized to transparent text color
TXT = Image.new('RGBA', BASE.size, (255,255,255,0))

# get a font
FNT = ImageFont.truetype('arial.ttf', 60)
# new drawing object
d = ImageDraw.Draw(TXT)

if __name__ == '__main__':
    # Loop that creates each unique photo
    POSITION = 0
    for i in range(AMOUNT):
        POSITION += STEP
        d.text((POSITION, 10), "SaveMyServer", font=FNT, fill=(0, 0, 0, OPACITY))
        out = Image.alpha_composite(BASE, TXT)
        out.save(NAME + "-watermarked-" + str(i + 1)+ "." + EXTENSION)
        TXT = Image.new('RGBA', BASE.size, (255, 255, 255, 0))
        d = ImageDraw.Draw(TXT)
        if i % AMOUNT // TOOLBAR_WIDTH == 0:
            for i in range((TOOLBAR_WIDTH // AMOUNT) + (TOOLBAR_WIDTH % AMOUNT)):
                sys.stdout.write("#")
                sys.stdout.flush()

    sys.stdout.write("\n")
