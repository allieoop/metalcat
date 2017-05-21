from scrapy.spiders import Spider
from scrapy.selector import HtmlXPathSelector
from metalcat.items import MetrolyricsItem

class MetrolyricsSpider(Spider):
    name = "metrolyrics_spider"
    allowed_domains = ["metrolyrics.com"]
    start_urls = ["http://www.metrolyrics.com/dopesmoker-lyrics-sleep.html"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        verses = hxs.select('//div[@id="lyrics-body-text"]/p[@class="verse"]')
        items = []
        for verse in verses:
            item = MetrolyricsItem()
            item['lines'] = verse.select('text()').extract()
            items.append(item)
        return items
