# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentspiderItem(scrapy.Item):
    # define the fields for your item here like:
    positionName = scrapy.Field()

    positionType = scrapy.Field()

    positionNum = scrapy.Field()

    positionLink = scrapy.Field()

    positionDesc = scrapy.Field()