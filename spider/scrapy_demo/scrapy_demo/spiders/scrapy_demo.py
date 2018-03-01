# -*- coding: utf-8 -*-

import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from spider.scrapy_demo.scrapy_demo.items import ScrapyDemoItem
from spider.scrapy_demo.scrapy_demo.items import ContentItem

class Mysplider(scrapy.Spider):
    name = 'scrapy_demo'
    allowed_domains = ['x23us.com']
    bash_url = 'http://www.x23us.com/class/'
    bashurl = '.html'

    def start_requests(self):
        for i in range(1, 11):
            url = self.bash_url + str(i) + '_1' + self.bashurl
            yield Request(url, self.parse)

    def parse(self, response):
        max_num = BeautifulSoup(response.text, 'lxml').find('div', class_='pagelink').find_all('a')[-1].get_text()
        bashurl = str(response.url)[:-7]
        for num in range(1, int(max_num) + 1):
            url = bashurl + '_' + str(num) + self.bashurl
            yield Request(url, callback=self.get_name)

    def get_name(self, response):
        tds = BeautifulSoup(response.text, 'lxml').find_all('tr', bgcolor='#FFFFFF')
        for td in tds:
            novel_name = td.find('a', target='_blank').get_text()
            novel_url = td.find('a')['href']
            #print(novel_name+':'+ novel_url)
            yield Request(novel_url, callback=self.get_chapter_url, meta={'name':novel_name, 'url': novel_url})

    def get_chapter_url(self, response):
        item = ScrapyDemoItem()
        item['name'] = str(response.meta['name']).replace('\xa0','')
        item['novel_url'] = response.meta['url']
        category = BeautifulSoup(response.text, 'lxml').find('table').find('a').get_text()
        author = BeautifulSoup(response.text,'lxml').find('table').find_all('td')[1].get_text()
        bash_url = BeautifulSoup(response.text, 'lxml').find('p', class_='btnlinks').find('a', class_='read')['href']
        item['category'] = str(category).replace('/','')
        item['author'] = str(author).replace('\xa0','').replace('/','')
        item['name_id'] = str(bash_url)[-6:-1].replace('/','')
        item['serial_status'] = 0
        item['serial_number'] = 0
        yield item
        yield Request(url=bash_url, callback=self.get_chapter, meta={'name_id': item['name_id']})

    def get_chapter(self, response):
        urls = re.findall(r'<td class="L"><a href="(.*?)">(.*?)</a></td>', response.text)
        num = 0
        for url in urls:
            num = num + 1
            chapter_url = response.url + url[0]
            chapter_name = url[1]
            yield Request(chapter_url, callback=self.get_chapter_content, meta={'num': num, 'name_id': response.meta['name_id'], 'chapter_name': chapter_name, 'chapter_url': chapter_url})

    def get_chapter_content(self, response):
        item = ContentItem()
        item['num'] = response.meta['num']
        item['name_id'] = response.meta['name_id']
        item['chapter_name'] = response.meta['chapter_name'].replace('\xa0','')
        item['chapter_url'] = response.meta['chapter_url']
        content = BeautifulSoup(response.text, 'lxml').find('dd', id='contents').get_text()
        item['chapter_content'] = str(content).replace('\xa0', '')
        return

