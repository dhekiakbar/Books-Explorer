# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Books3Item(scrapy.Item):
    name = scrapy.Field(name="Not Found")
    price = scrapy.Field(price="Rp.0")
    stock = scrapy.Field(stock="0/0")
    # define the fields for your item here like:
    # name = scrapy.Field()
