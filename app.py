import os
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
    overlayLyricsOnCatPhoto()
    return render_template('index.html')

def overlayLyricsOnCatPhoto():
    with open('output/lyrics.json') as json_data:
        verses = json.load(json_data)
        first_line = verses[0]['lines'][0]
        second_line = verses[0]['lines'][1]

    img = Image.open("static/cat.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('static/Impact.ttf', 60)
    draw.text((25, 50), first_line, (200,40,40), font=font)
    draw.text((75, 100), second_line, (200,40,40), font=font)
    img.save('output/metalcat.jpg')

if __name__ == "__main__":
    app.run()
