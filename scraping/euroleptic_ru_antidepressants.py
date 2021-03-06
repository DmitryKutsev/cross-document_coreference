from time import sleep
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys

# https://neuroleptic.ru/forum/forum/2-%D0%BD%D0%B5%D0%B9%D1%80%D0%BE%D0%BB%D0%B5%D0%BF%D1%82%D0%B8%D0%BA%D0%B8/
print(os.getcwd())
driver = webdriver.Chrome('/home/cola-pirat/hse/diplom_corpus/cross-document_coreference/scraping/chromedriver')
driver.get(f'https://neuroleptic.ru/forum/forum/6-%D0%B0%D0%BD%D1%82%D0%B8%D0%B4%D0%B5%D0%BF%D1%80%D0%B5%D1%81%D1%81%D0%B0%D0%BD%D1%82%D1%8B/')
# topic_title
topics = []
for i in range(6):
    local_link = f'https://neuroleptic.ru/forum/forum/6-%D0%B0%D0%BD%D1%82%D0%B8%D0%B4%D0%B5%D0%BF%D1%80%D0%B5%D1%81%D1%81%D0%B0%D0%BD%D1%82%D1%8B/page-{i+1}'
    driver.get(local_link)
    local_topics = driver.find_elements_by_class_name('topic_title')
    local_topics = [topic.get_attribute('href') for topic in local_topics]
    topics.extend(local_topics)

handler = open('neuroleptic_antidepr2.txt', 'a', encoding='utf-8')


for topic in topics:
    handler.write('\nTOPIC\n')
    driver.get(topic)
    number_of_strings = driver.find_elements_by_partial_link_text('Страница')
    if len(number_of_strings)>0:
        number_of_strings = number_of_strings[0].text[-1]
        number_of_strings = int(number_of_strings)
        for i in range(number_of_strings + 1):
            driver.get(topic + f'page-{i}')
            posts = driver.find_elements_by_css_selector("div.post.entry-content")
            for post in posts:
                handler.write(post.text)
                handler.write('\n----\n')
driver.close()
handler.close()

