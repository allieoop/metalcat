import argparse
import os
import datetime
import json
import scrapy
from scrapy.crawler import CrawlerProcess
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

import metalcat
from metalcat.spiders.metrolyrics_spider import MetrolyricsSpider

def overlayLyricsOnCatImage():
    overlay_text = getOverlayText();
    img = Image.open('static/cat.png')
    draw = ImageDraw.Draw(img)
    width, height = img.size
    text_color = (200,40,40)
    font = getFittedFont(width, overlay_text[0])
    draw.text((50, 50), overlay_text[0], text_color, font=font)
    font = getFittedFont(width, overlay_text[1])
    draw.text((80, 100), overlay_text[1], text_color, font=font)
    date_string = datetime.datetime.now().strftime('-%d%H%M%S')
    img.save('output/metalcat'+date_string+'.jpg')

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
        for verse in verses:
            lines = verse['lines']
            if len(lines) >= 2:
                overlay_text[0] = lines[0]
                overlay_text[1] = lines[1]
                break
    return overlay_text

def crawl(song, artist):
    if os.path.isfile('output/lyrics.json'):
        os.remove('output/lyrics.json')

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'FEED_FORMAT': 'json',
        'FEED_URI': 'output/lyrics.json',
        'FEED_EXPORT_ENCODING':'utf-8'
    })

    process.crawl(MetrolyricsSpider, song=song, artist=artist)
    process.start()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s',
                        '--song',
                        help='The name of a song, with dashes instead of spaces',
                        default='dopesmoker',
                        required=False)
    parser.add_argument('-a',
                        '--artist',
                        help='The name of an artist, with dashes instead of spaces',
                        default='sleep',
                        required=False)
    args = parser.parse_args()

    crawl(args.song, args.artist)
    overlayLyricsOnCatImage()

if __name__ == "__main__":
    main()

