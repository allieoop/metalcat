from scrapy.item import Item, Field

class MetrolyricsItem(Item):
    lines = Field()