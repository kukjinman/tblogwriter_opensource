from selenium import webdriver

def init_browser(url_input):
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=opt)
    url = url_input
    browser.get(url)
    browser.maximize_window()
    return browser
