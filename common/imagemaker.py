import datetime
import glob
import json
import logging
import os
import random
import shutil
from io import BytesIO

import requests
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

SCRAPED_ITEMS_FILE = 'output/lyrics.json'
NORMAL_CAT_DIR = 'static/normalcats/'
NORMAL_CATS_FILE = 'static/normalcats.json'
METAL_CAT_ARCHIVE = 'static/metalcats/archive/'
DEFAULT_IMAGE_URL = 'http://i.imgur.com/aeweLdr.jpg'
FONT_TYPE = 'static/Impact.ttf'

def get_image(image_url="", image_file_path=""):
    if image_url:
        response = requests.get(image_url)
        return BytesIO(response.content)
    elif image_file_path:
        return image_file_path
    else:
        url = select_random_image_url()
        response = requests.get(url)
        return BytesIO(response.content)

def get_overlay_text(song, artist):
    overlay_text = [' ', 'meow meow meow meow']
    lyrics = get_lyrics(song, artist)
    if not lyrics:
        return overlay_text

    verse = random.choice(lyrics)
    if len(verse) < 2:
        # try a second time
        verse = random.choice(lyrics)

        # try a third time, but by going through all lyrics
        if len(verse) < 2:
            for v in lyrics:
                if len(v) >= 2:
                    verse = v

    if len(verse) >= 2:
        first_line = random.choice(verse)
        second_line_index = verse.index(first_line)+1
        if second_line_index < len(verse):
            overlay_text = [first_line, verse[second_line_index]]
        else:
            overlay_text = [verse[0], verse[1]]

    return overlay_text

def delete_images(images_dir):
    for the_file in os.listdir(images_dir):
        file_path = os.path.join(images_dir, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

def archive_image(image_path):
    archive_path = os.path.join(METAL_CAT_ARCHIVE, os.path.basename(image_path))
    shutil.move(image_path, archive_path)
    return archive_path

def draw_text_on_image(image_path, overlay_text):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    width, height = img.size
    text_color = (200,40,40)
    font = get_fitted_font(width, overlay_text[0])
    x0_1 = (int) (width * 0.02)
    y0_1 = (int) (font.getsize('A')[0] / 2)
    draw.text((x0_1, y0_1), overlay_text[0].strip(), text_color, font=font)
    font = get_fitted_font(width, overlay_text[1])
    x0_2 = (int) (width * 0.04)
    y0_2 = (int) (height - font.getsize('A')[1] * 1.5)
    draw.text((x0_2, y0_2), overlay_text[1].strip(), text_color, font=font)
    date_string = datetime.datetime.now().strftime('%d%H%M%S')
    image_name = 'static/metalcats/'+date_string+'.jpg'
    img.save(image_name)
    return image_name

def select_random_image_url():
    with open(NORMAL_CATS_FILE) as json_file:
        for line in json_file:
            normal_cats_json = json.loads(line)
            return random.choice(normal_cats_json['urls'])
    return DEFAULT_IMAGE_URL

def select_random_image():
    return random.choice(get_cat_images(NORMAL_CAT_DIR))

def get_cat_images(image_dir):
    accepted_file_extensions = ('.jpg', '.jpeg', '.png')
    files = []
    for extension in accepted_file_extensions:
        files.extend(glob.glob(image_dir+'*'+extension))
    return files

def get_fitted_font(image_width, overlay_text):
    fontsize = 1
    image_fraction = 0.90 # portion of the image width that the text will cover
    # iterate until the text size is just larger than the criteria
    font = ImageFont.truetype(FONT_TYPE, fontsize)
    while font.getsize(overlay_text)[0] < image_fraction*image_width:
        fontsize += 1
        font = ImageFont.truetype(FONT_TYPE, fontsize)
    # Decrement to be sure it is less than criteria
    fontsize -= 1
    return ImageFont.truetype(FONT_TYPE, fontsize)

def song_lyrics_exist(song, artist):
    if not os.path.isfile(SCRAPED_ITEMS_FILE):
        return 0

    with open(SCRAPED_ITEMS_FILE) as json_file:
        for line in json_file:
            item = json.loads(line)
            if item['song'] == song and item['artist'] == artist:
                return 1
    return 0

def get_lyrics(song, artist):
    if not os.path.isfile(SCRAPED_ITEMS_FILE):
        return []
    with open(SCRAPED_ITEMS_FILE) as json_file:
        for line in json_file:
            item = json.loads(line)
            if item['song'] == song and item['artist'] == artist:
                return item['lyrics']
    return []