import json
import os

from billiard import Process
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from metalcat.spiders.metrolyrics_spider import MetrolyricsSpider

class SpiderRunner(Process):
    def __init__(self, spider, song, artist, feed_uri):
        Process.__init__(self)
        settings = Settings({
            'USER_AGENT': 'MetalCatSpider',
            'FEED_FORMAT': 'jsonlines',
            'FEED_URI': feed_uri,
            'FEED_EXPORT_ENCODING':'utf-8'
        })
        self.song = song
        self.artist = artist
        self.crawler = CrawlerProcess(settings)
        self.spider = spider

    def run(self):
        self.crawler.crawl(self.spider, song=self.song, artist=self.artist)
        self.crawler.start()

def item_exists(song, artist, feed_uri):
    if not os.path.isfile(feed_uri):
        return 0

    with open(feed_uri) as json_file:
        for line in json_file:
            item = json.loads(line)
            if item['song'] == song and item['artist'] == artist:
                return 1
    return 0

def run_spider(song, artist, feed_uri):
    spider = MetrolyricsSpider(song, artist)
    spider_runner = SpiderRunner(spider, song, artist, feed_uri)
    spider_runner.start()
    spider_runner.join()