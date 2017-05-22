import os
import json
import scrapy
from scrapy.crawler import CrawlerProcess
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from flask import Flask

import metalcat
from metalcat.spiders.metrolyrics_spider import MetrolyricsSpider

app = Flask(__name__)
app.config.update(DEBUG = True)

@app.route("/")
def main():
    with open('lyrics.json') as json_data:
        verses = json.load(json_data)
        first_line = verses[0]['lines'][0]
        second_line = verses[0]['lines'][1]

    img = Image.open("cat.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('Impact.ttf', 60)
    draw.text((25, 50), first_line, (200,40,40), font=font)
    draw.text((75, 100), second_line, (200,40,40), font=font)
    img.save('metalcat.jpg')

    return "metalcat!"

if __name__ == "__main__":
    app.run()
