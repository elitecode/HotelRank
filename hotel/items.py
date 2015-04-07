# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HotelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
    nReviews = scrapy.Field()
    pass

class ReviewItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    review = scrapy.Field()
    pass