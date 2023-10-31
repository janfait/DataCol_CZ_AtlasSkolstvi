# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SchoolItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    identifier = scrapy.Field()
    address = scrapy.Field()
    email = scrapy.Field()
    phone = scrapy.Field()
    website = scrapy.Field()
    description = scrapy.Field()
    
