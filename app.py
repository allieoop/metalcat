import os
import datetime
import json
import scrapy
from scrapy.crawler import CrawlerProcess
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from flask import Flask, render_template

import metalcat
from metalcat.spiders.metrolyrics_spider import MetrolyricsSpider

app = Flask(__name__)
app.config.update(DEBUG = True)

@app.route("/")
def main():
    overlayLyricsOnCatImage()
    return render_template('index.html')

def overlayLyricsOnCatImage():
    overlay_text = getOverlayText();
    img = Image.open('static/cat.png')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('static/Impact.ttf', 60)
    draw.text((50, 50), overlay_text[0], (200,40,40), font=font)
    draw.text((80, 100), overlay_text[1], (200,40,40), font=font)
    date_string = datetime.datetime.now().strftime('-%d%H%M%S')
    img.save('output/metalcat'+date_string+'.jpg')

def getOverlayText():
    overlay_text = ['=^..^=', '']
    with open('output/lyrics.json') as json_data:
        verses = json.load(json_data)
        for verse in verses:
            lines = verse['lines']
            if len(lines) >= 2:
                if (len(lines[0]) < 47 and len(lines[1]) < 47):
                    overlay_text[0] = lines[0]
                    overlay_text[1] = lines[1]
                    break
    return overlay_text

if __name__ == "__main__":
    app.run()
