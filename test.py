import json
import scrapy
from scrapy.crawler import CrawlerProcess

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

import metalcat
from metalcat.spiders.metrolyrics_spider import MetrolyricsSpider

if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'FEED_FORMAT': 'json',
        'FEED_URI': 'lyrics.json',
        'FEED_EXPORT_ENCODING':'utf-8'
    })

    process.crawl(MetrolyricsSpider)
    lyrics_json = process.start()

    with open('lyrics.json') as json_data:
        d = json.load(json_data)
        first_line = d[0]['lines'][0]
        second_line = d[0]['lines'][1]

    img = Image.open("cat.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('/Library/Fonts/Impact.ttf', 60)
    draw.text((25, 50), first_line, (200,40,40), font=font)
    draw.text((100, 100), second_line, (200,40,40), font=font)
    img.save('metalcat.jpg')

