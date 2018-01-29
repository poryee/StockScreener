# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AiscreenerItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    currency = scrapy.Field()
    price = scrapy.Field()
    year_low = scrapy.Field()
    year_high = scrapy.Field()
    marketcap = scrapy.Field()
    pe_ratio = scrapy.Field()
    bookvalue = scrapy.Field()
    pb_ratio = scrapy.Field()
    trailingdivident = scrapy.Field()
    PEG = scrapy.Field()
