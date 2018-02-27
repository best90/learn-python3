# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 小说
    name = scrapy.Field()
    #作者
    author = scrapy.Field()
    #小说地址
    novel_url = scrapy.Field()
    #状态
    serial_status = scrapy.Field()
    #连载字数
    serial_number = scrapy.Field()
    #分类
    category = scrapy.Field()
    #小说编号
    name_id = scrapy.Field()
    pass
