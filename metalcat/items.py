from scrapy.item import Item, Field

class MetrolyricsItem(Item):
	song = Field()
	artist = Field()
	lyrics = Field()