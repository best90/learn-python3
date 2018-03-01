# -*- coding: utf-8 -*-

import mysql.connector
from spider.scrapy_demo.scrapy_demo import settings

MYSQL_HOST = settings.MYSQL_HOST
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_DB = settings.MYSQL_DB

connect = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOST, port=MYSQL_PORT, database=MYSQL_DB)
cur = connect.cursor(buffered=True)

class Sql:

    @classmethod
    def insert_novel(cls, name, author, category, name_id):
        sql = 'INSERT INTO novel(`name`, `author`, `category`, `name_id`) VALUES (%(name)s,%(author)s,%(category)s,%(name_id)s)'
        value  = {
            'name': name,
            'author': author,
            'category': category,
            'name_id': name_id
        }
        cur.execute(sql, value)
        connect.commit()

    @classmethod
    def select_name(cls, name_id):
        sql = 'SELECT EXISTS(SELECT 1 FROM novel WHERE name_id=%(name_id)s)'
        value = {
            'name_id': name_id
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]

    @classmethod
    def insert_chapter(cls, chapter_name, content, name_id, num_id, url):
        sql = 'INSERT INTO novel_chapter(`chapter_name`, `content`, `name_id`, `num_id`, `url`) VALUES (%(chapter_name)s,%(content)s,%(name_id)s,%(num_id)s,%(url)s)'
        value  = {
            'chapter_name': chapter_name,
            'content': content,
            'name_id': name_id,
            'num_id': num_id,
            'url': url
        }
        cur.execute(sql, value)
        connect.commit()

    @classmethod
    def select_chapter(cls, url):
        sql = 'SELECT EXISTS(SELECT 1 FROM novel_chapter WHERE url=%(url)s)'
        value = {
            'url': url
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]