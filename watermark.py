'''
This script takes a jpg image and creates multiple copies. Each of which
has a watermark that is not visible to the naked eye. The watermark on 
each of the images is shifted slightly in location from the previous image.
This makes each image optically unique as well as produce a different has value

'''
import os
from PIL import Image, ImageDraw, ImageFont

# Directory where images should be placed
LOCATION = '//nas-r510/D$/Pictures/Watermark/'
# Getting the last occurrence of the period to get file EXTENSION
##LAST_DOT = IMG_FILES.rfind('.')
# Splitting the file into file name and EXTENSION name
##NAME = IMG_FILES[:LAST_DOT]
##EXTENSION = IMG_FILES[LAST_DOT+1:]
# opens image file


#TODO: finish collecting variables to put in the multi_watermark function
#TODO: make function to get file and path info and testing path correctness

def pick_image_from(img_files,choice=1):
    '''
    Prompts user to pick an image file to be used and returns that file
    '''
    return img_files[0][choice-1],img_files[1]


def get_image_files(location):
    '''
    Given a file path the function returns the image files in that directory

    TODO:
    - Test given file path
    - get all image files in the given directory
    - return image files
    '''
    file_extensions = ['.jpg','.png']
    path_exists = os.path.exists(location)
    img_files = []

    if path_exists:
        # finding a file in the current directory that is a jpeg
        files = os.listdir(location)
        for f in files:
            for e in file_extensions:
                if e in f:
                    img_files.append(f)

    return img_files, location


def multi_watermark(img_file, amount, txt='SaveMyServer'):
    '''
    Takes an image and makes multiple copies with a watermark

    not pure function
    '''
    # Opening the image file to begin manipulation
    base_image = Image.open(img_file[1] + img_file[0]).convert('RGBA')
    # Getting file name and extension for use when saving the file
    delimiter = img_file[0].rfind('.')
    file_name = img_file[0][:delimiter]
    file_extension = img_file[0][delimiter+1:]
    out_directory = img_file[1] + 'watermarked_' + file_name
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
        out.save(out_directory + '/' + file_name + "-watermarked-" + str(i + 1)+ "." + file_extension)

if __name__ == '__main__':
    AMOUNT = int(input("How many copies would you like?\nEnter number: "))
    IMG_FILES = get_image_files(LOCATION)
    BASE_IMG = pick_image_from(IMG_FILES)
    multi_watermark(BASE_IMG, AMOUNT)
