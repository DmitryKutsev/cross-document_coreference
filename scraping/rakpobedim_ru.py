from time import sleep
import os
from selenium import webdriver

driver = webdriver.Chrome('/home/cola-pirat/hse/diplom_corpus/cross-document_coreference/scraping/chromedriver')
topics = []

for i in range(10):
    local_link = f'http://www.rakpobedim.ru/forum/index.php?/forum/6-%d1%87%d0%b5%d0%bc-%d' \
                 f'0%b8-%d0%ba%d0%b0%d0%ba-%d0%bb%d0%b5%d1%87%d0%b8%d0%bc%d1%81%d1%8f' \
                 f'/page__prune_day__100__sort_by__Z-A__sort_key__last_post__topicfilter__all__st__{i*30}'
    driver.get(local_link)

    # sleep(2)
    local_topics = driver.find_elements_by_class_name('topic_title')
    local_topics = [topic.get_attribute('href') for topic in local_topics]
    topics.extend(local_topics)

handler = open('rakpobedim_ru.txt', 'a', encoding='utf-8')

for topic in topics:
    driver.get(topic)
    stop = 1
    while stop:
        next_string = driver.find_elements_by_class_name('next')
        if len(next_string) > 0:
                driver.get(topic + f'page__st__{i * 20}')
                posts = driver.find_elements_by_css_selector("div.post.entry-content")
                for post in posts:
                    # print(post.text)
                    handler.write(post.text)
                    handler.write('\n----\n')
                stop += 1
        else:
            stop = None
    else:
        driver.get(topic)
        sleep(2)
        posts = driver.find_elements_by_css_selector("div.post.entry-content")
        for post in posts:
            # print(post.text)
            handler.write(post.text)
            handler.write('\n----\n')

driver.close()
handler.close()