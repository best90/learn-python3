# -*- coding: utf-8 -*-

from .sql import Sql
from spider.scrapy_demo.scrapy_demo.items import ScrapyDemoItem

class DemoPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item, ScrapyDemoItem):
            name_id = item['name_id']
            result = Sql.select_name(name_id)
            if result[0] == 1:
                print('已经存在了')
                pass
            else:
                name = item['name']
                author = item['author']
                category = item['category']
                Sql.insert_novel(name, author, category, name_id)
                print('开始保存小说：', name)