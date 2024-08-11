from time import sleep

from selenium import webdriver

from selenium_util import init_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def cralwingheadlinePost(browser_):

    contents = []

    headline_a = WebDriverWait(browser_,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"#wp--skip-link--target > div > div.wp-block-columns.alignfull.is-layout-flex.wp-container-core-columns-is-layout-42.wp-block-columns-is-layout-flex > div:nth-child(1) > section > div > div:nth-child(1) > div > div > div > h2 > a"))
    )
    headline_href = headline_a.get_attribute("href")
    browser_.get(headline_href)

    headline_h1 = WebDriverWait(browser_,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"#wp--skip-link--target > div > div.wp-block-columns.alignfull.is-layout-flex.wp-container-core-columns-is-layout-61.wp-block-columns-is-layout-flex > div.wp-block-column.single-post__container.is-layout-flow.wp-block-column-is-layout-flow > div > div.wp-block-template-part > div > h1"))
    )
    # print("h1 : " + headline_h1.text)
    contents.append(headline_h1.text)

    headline_ps = WebDriverWait(browser_,10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR,"#wp--skip-link--target > div > div.wp-block-columns.alignfull.is-layout-flex.wp-container-core-columns-is-layout-61.wp-block-columns-is-layout-flex > div.wp-block-column.single-post__container.is-layout-flow.wp-block-column-is-layout-flow > div > div.entry-content.wp-block-post-content.is-layout-flow.wp-block-post-content-is-layout-flow p"))
        )

    for idx,p in enumerate(headline_ps):
        # print("[" + str(idx) + "] : " + p.text)
        contents.append(p.text)

    # print(contents)
    return contents



def runCrawlingManager():
    browser = init_browser("https://techcrunch.com/")
    contents_result = cralwingheadlinePost(browser)
    browser.quit()
    return contents_result