from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# https://mneploho.net
# https://mneploho.net/forum/1002-32
driver = webdriver.Chrome('./chromedriver')
for i in range(32):

    driver.get(f'https://mneploho.net/forum/1002-{i}')
    sleep(4)
    tread_links = driver.find_elements_by_class_name('thread_link')
    hrefs = []
    # treads on the front page
    for el in tread_links:
        local_href = el.find_element_by_tag_name('a').get_attribute('href')
        hrefs.append(local_href)

    # messages in tread(one page)
    handler = open('mneploho_net.txt', 'a', encoding='utf-8')
    all_elements = []
    for href in hrefs:
        driver.get(href)
        elems = driver.find_elements_by_class_name('post_content')
        for i in elems:
            handler.write(i.text)
            handler.write('\n----\n')
        next = driver.find_elements_by_partial_link_text('Следующая')
        # one element, not list
        if len(next) > 0:
            next_href = driver.find_element_by_partial_link_text('Следующая').get_attribute('href')
            driver.get(next_href)
            while(len(next) > 0):
                driver.get(next_href)
                elems = driver.find_elements_by_class_name('post_content')
                for i in elems:
                    handler.write(i.text)
                    handler.write('\n----\n')
                next = driver.find_elements_by_partial_link_text('Следующая')
                if len(next) > 0:
                    next_href = driver.find_element_by_partial_link_text('Следующая').get_attribute('href')

driver.close()
handler.close()