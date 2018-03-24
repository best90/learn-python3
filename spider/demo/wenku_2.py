# -*- coding:UTF-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time

if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
    driver = webdriver.Chrome('D:\Program Files\Python3\Scripts\chromedriver.exe', chrome_options=option)
    driver.get('https://wk.baidu.com/view/8d33da51ad02de80d4d8407f')

    html = driver.page_source
    bs = BeautifulSoup(html,'lxml')
    result = bs.find_all(class_='sf-edu-wenku-id-container')
    bs2 = BeautifulSoup(str(result[0]), 'lxml')
    title = bs2.find('div', class_='doc-title').text
    print('文章标题：%s' % title)

    n = 1
    while True:
        bs = BeautifulSoup(html, 'lxml')
        if n == 1:
            continue_read = driver.find_element_by_xpath("//div[@class='foldpagewg-text-con']")
            continue_read.click()
            n = n - 1
            page_part = bs.find_all(class_='pagerwg-schedule')
            page_part = BeautifulSoup(str(page_part[0]), 'lxml').text
            page_pattern = re.compile('已读(\d+)%')
            num = int(page_pattern.findall(page_part)[0])
            click_next_count = 100 / num
            time.sleep(1)

        button = bs.find_all(class_='pagerwg-button')
        if len(button) > 0 and click_next_count > 1:
            scroll_point = driver.find_element_by_xpath("//div[@class='pagerwg-schedule']")
            driver.execute_script("arguments[0].scrollIntoView();", scroll_point)
            next_page = driver.find_element_by_xpath("//div[@class='pagerwg-button']")
            next_page.click()
            click_next_count = click_next_count - 1
            time.sleep(2)
            html = driver.page_source
        else:
            result = bs.find_all(class_='rtcspage')
            for each_result in result:
                bs2 = BeautifulSoup(str(each_result), 'lxml')
                text = bs2.find_all('p')
                for each_text in text:
                    main_body = BeautifulSoup(str(each_text), 'lxml')
                    for each in main_body.find_all(True):
                        if each.name == 'span':
                            print(each.text.replace('\xa0', ''), end='')
                        elif each.name == 'br':
                            print('')
                    print(main_body.text)
                print('\n')
            break