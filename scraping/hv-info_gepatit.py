

# https://www.hv-info.ru/!!!!!!!!

from time import sleep
import os
from selenium import webdriver

driver = webdriver.Chrome('/home/cola-pirat/hse/diplom_corpus/cross-document_coreference/scraping/chromedriver')
topics = []

handler = open('hv-info_gepatit.txt', 'a', encoding='utf-8')

for i in range(10):
    local_link = f'https://www.hv-info.ru/gepatit-forum/viewforum.php?f=22&start={i*50}'
    driver.get(local_link)
    local_topics = driver.find_elements_by_class_name('topictitle')
    local_topics = [topic.get_attribute('href') for topic in local_topics]
    topics.extend(local_topics)

    for topic in topics:

        stop = 0
        while stop != 'up':
            driver.get(f'{topic}&start={stop*15}')

            btns = driver.find_elements_by_class_name('fa-chevron-right')
            posts = driver.find_elements_by_class_name('content')
            for post in posts:
                # print(post.text)
                handler.write(post.text)
                handler.write('\n----\n')

            stop += 1
            if len(btns) == 0 or stop == 20:
                stop = 'up'


driver.close()
handler.close()