# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CeicdataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #定义爬虫数据结构
    level = scrapy.Field() #地震级别
    time = scrapy.Field() #发震时间
    lat = scrapy.Field() #纬度
    lon = scrapy.Field() #经度
    deep = scrapy.Field() #深度
    position = scrapy.Field() #参考位置
    did = scrapy.Field() #数据ID
    

    pass
