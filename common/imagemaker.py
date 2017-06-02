import datetime
import glob
import json
import logging
import os
import random
from io import BytesIO

import requests
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def selectImage(image_url, image_file_path=""):
    image_directory = 'static/normalcats/'
    image = image_directory + 'default_cat.png'
    random_image = selectRandomImage(image_directory)
    if image_url:
        response = requests.get(image_url)
        image = BytesIO(response.content)
        # TODO: Do some error checking
    elif image_file_path:
        image = image_file_path
    elif random_image:
        image = random_image
    return image

def selectRandomImage(image_directory):
    accepted_file_extensions = ('.jpg', '.jpeg', '.png')
    files = []
    for extension in accepted_file_extensions:
        files.extend(glob.glob(image_directory+'*'+extension))
    image = random.choice(files)
    return image

def overlayLyrics(image_path):
    overlay_text = getOverlayText();
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    width, height = img.size
    text_color = (200,40,40)
    font = getFittedFont(width, overlay_text[0])
    x0_1 = (int) (width * 0.02)
    y0_1 = (int) (font.getsize('A')[0] / 2)
    draw.text((x0_1, y0_1), overlay_text[0].strip(), text_color, font=font)
    font = getFittedFont(width, overlay_text[1])
    x0_2 = (int) (width * 0.04)
    y0_2 = (int) (height - font.getsize('A')[1] * 1.5)
    draw.text((x0_2, y0_2), overlay_text[1].strip(), text_color, font=font)
    date_string = datetime.datetime.now().strftime('%d%H%M%S')
    image_name = 'static/metalcats/'+date_string+'.jpg'
    img.save(image_name)
    return image_name

def getFittedFont(image_width, overlay_text):
    fontsize = 1
    image_fraction = 0.90 # portion of the image width that the text will cover
    # iterate until the text size is just larger than the criteria
    font = ImageFont.truetype("static/Impact.ttf", fontsize)
    while font.getsize(overlay_text)[0] < image_fraction*image_width:
        fontsize += 1
        font = ImageFont.truetype("static/Impact.ttf", fontsize)
    # Decrement to be sure it is less than criteria
    fontsize -= 1
    return ImageFont.truetype("static/Impact.ttf", fontsize)

def getOverlayText():
    overlay_text = ['=^..^=', '']
    with open('output/lyrics.json') as json_data:
        verses = json.load(json_data)
        verse = random.choice(verses)
        lines = verse['lines']
        if len(lines) >= 2:
            first_line = random.choice(lines)
            second_line_index = lines.index(first_line)+1
            if second_line_index < len(lines):
                overlay_text[0] = first_line
                overlay_text[1] = lines[second_line_index]
            else:
                overlay_text[0] = lines[0]
                overlay_text[1] = lines[1]
    return overlay_text