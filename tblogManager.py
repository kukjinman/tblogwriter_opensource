from time import sleep

from selenium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from selenium_util import init_browser

my_id = "add your tblog id"
my_password = "add your tblog password"



def login_to_kakao():
    login_btn = browser.find_element(By.CSS_SELECTOR,"a.btn_login.link_kakao_id span.txt_login")
    login_btn.click()
    sleep(0.5)
    kakao_id = browser.find_element(By.CSS_SELECTOR,"#loginId--1")
    kakao_id.send_keys(my_id)
    kakao_password = browser.find_element(By.CSS_SELECTOR,"#password--2")
    kakao_password.send_keys(my_password)
    kakao_login_btn = browser.find_element(By.CSS_SELECTOR,"#mainContent > div > div > form > div.confirm_btn > button.btn_g.highlight.submit")
    kakao_login_btn.click()
    sleep(0.5)

def navigate_to_newpost():
    newpost_a = browser.find_element(By.CSS_SELECTOR,"div > div:nth-child(3) > a.img_common_tistory.link_edit")
    newpost_href = newpost_a.get_attribute("href")
    browser.get(newpost_href)
    sleep(1)
    try:
        newpost_alert = browser.switch_to.alert
        newpost_alert.dismiss()
    except NoAlertPresentException:
        print("NoAlertPresentException")


def runtblogManager():
    global browser
    browser = init_browser("https://www.tistory.com/auth/login")
    login_to_kakao()
    navigate_to_newpost()

def writeContentByGptResult(gpt_res):
    print("writeContentByGptResult is called")
    print("gpt res : ", gpt_res)
    global newpost_body
    frame_flag = False

    gpt_res_tmp = gpt_res.split(".")
    print("gpt res tmp : ", gpt_res_tmp)

    for idx,i in enumerate(gpt_res_tmp):
        print(idx)
        print("i : ", i+".")

        if idx == 0:
            newpost_title = browser.find_element(By.CSS_SELECTOR,"#post-title-inp")
            newpost_title.send_keys(i+".")
        else:
            if frame_flag == False:
                browser.switch_to.frame("editor-tistory_ifr")
                frame_flag = True

            newpost_body = browser.find_element(By.CSS_SELECTOR,"#tinymce")
            newpost_body.send_keys(i+".")


def bodystyling_update():
    print("bodystyling_update is called")

    ActionChains(browser).click(newpost_body)
    ActionChains(browser).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

    browser.switch_to.default_content()

    font_size_btn = browser.find_element(By.CSS_SELECTOR,"#mceu_1-open")
    font_size_btn.click()

    font_mainsize1_btn = browser.find_element(By.CSS_SELECTOR,"#mceu_35")
    font_mainsize1_btn.click()

    center_align_btn = browser.find_element(By.CSS_SELECTOR,"#mceu_10-button")
    center_align_btn.click()

def publish_newpost():
    print("publish_newpost is called")
    publish_btn = browser.find_element(By.CSS_SELECTOR,"#publish-layer-btn")
    publish_btn.click()

    public_btn = browser.find_element(By.CSS_SELECTOR,"#open20")
    public_btn.click()

    current_btn = browser.find_element(By.CSS_SELECTOR,"#editor-root > div:nth-child(42) > div > div > div > form > fieldset > div.layer_body > div > dl:nth-child(4) > dd > button.btn_date.on")
    current_btn.click()

    publish_complete_btn = browser.find_element(By.CSS_SELECTOR,"#publish-btn")
    publish_complete_btn.click()





