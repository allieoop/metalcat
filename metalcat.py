import argparse
import json
import logging
import os

from scrapy.crawler import CrawlerProcess

from common.imagemaker import overlayLyrics, selectImage
from metalcat.spiders.metrolyrics_spider import MetrolyricsSpider

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
    cat_logo = """     
       /\ /\ 
      > ^ ^ < 
    \m/  `  \m/ 
      \ / \ / 
       (___)_____ 
    """
    print(cat_logo)

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
    parser.add_argument('-i',
                        '--image',
                        help='The image filepath',
                        default='',
                        required=False)
    parser.add_argument('-u',
                        '--url',
                        help='The image url',
                        default='',
                        required=False)
    args = parser.parse_args()

    # TODO: Check if file exists if no song or artist is passed - don't crawl every time
    crawl(args.song, args.artist)
    image = selectImage(args.url, args.image)
    overlayLyrics(image)

if __name__ == "__main__":
    logging.getLogger('PIL').setLevel(logging.WARNING)
    logging.getLogger('requests').setLevel(logging.WARNING)
    main()

