import logging

from scrapy import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import Spider

from metalcat.items import MetrolyricsItem

class MetrolyricsSpider(Spider):
    name = "metrolyrics_spider"
    allowed_domains = ["metrolyrics.com"]

    logging.getLogger('scrapy').setLevel(logging.WARNING)
    logging.getLogger('scrapy').propagate = False

    def __init__(self, song='space-time', artist='gojira', *args, **kwargs):
        super(MetrolyricsSpider, self).__init__(*args, **kwargs)
        self.song = song
        self.artist = artist

    def start_requests(self):
        url = 'http://www.metrolyrics.com/'+self.song+'-lyrics-'+self.artist+'.html'
        yield Request(url, self.parse)

    def parse(self, response):
        verses = response.xpath('//div[@id="lyrics-body-text"]/p[@class="verse"]')
        lyrics = []
        for verse in verses:
            lyrics.append(verse.xpath('text()').extract())
        metrolyrics_song = MetrolyricsItem()
        metrolyrics_song['song'] = self.song
        metrolyrics_song['artist'] = self.artist
        metrolyrics_song['lyrics'] = lyrics
        return metrolyrics_song
