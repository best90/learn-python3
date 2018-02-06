#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from spider.baike import url_manager
from spider.baike import html_downloader
from spider.baike import html_parser
from spider.baike import html_output

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = html_output.HtmlOutput()

    def crawl(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("crawl %d : %s" % (count, new_url))
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_data)

                if count == 10:
                    break
                count = count + 1
            except Exception as ex:
                print("crawl failed: %s" % ex.message())

        self.output.output_html()


if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/item/Python/407313'
    spider = SpiderMain()
    spider.crawl(root_url)