# -*- coding:UTF-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time

if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
    driver = webdriver.Chrome('D:\Program Files\Python3\Scripts\chromedriver.exe', chrome_options=option)
    driver.get('https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html')

    html = driver.page_source
    bs = BeautifulSoup(html,'lxml')
    result = bs.find_all(class_='sf-edu-wenku-id-container')
    bs2 = BeautifulSoup(str(result[0]), 'lxml')
    title = bs2.find('div', class_='doc-title').text
    page_num = bs.find_all(class_='page_mark')
    page_num = BeautifulSoup(str(page_num[0]), 'lxml').text
    page_pattern = re.compile('/(\d+)页')
    num = int(page_pattern.findall(page_num)[0])
    print('文章标题：%s' % title)
    print('文章页数：%d' % num)

    while True:
        num = num / 5.0
        html = driver.page_source
        bs = BeautifulSoup(html, 'lxml')
        result = bs.find_all(class_='singlePage')
        for each_result in result:
            bs2 = BeautifulSoup(str(each_result), 'lxml')
            text = bs2.find_all('p')
            for each_text in text:
                main_body = BeautifulSoup(str(each_text), 'lxml')
                for each in main_body.find_all(True):
                    if each.name == 'span':
                        print(each.string.replace('\xa0', ''), end='')
                    elif each.name == 'br':
                        print('')
                print(main_body.text)
            print('\n')
        # TODO: 翻页报错，待解决
        if num > 1:
            page = driver.find_element_by_xpath("//div[@class='x-page next']")
            driver.execute_script('arguments[0].scrollIntoView();',page[-1])
            next_page = driver.find_element_by_xpath("//span[@class='next-text']")
            next_page.click()
            time.sleep(3)
        else:
            break