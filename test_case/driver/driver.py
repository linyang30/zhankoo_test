from selenium import webdriver

def browser():
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('permissions.default.stylesheet', 2)
    firefox_profile.set_preference('permissions.default.image', 2)
    firefox_profile.update_preferences()
    driver = webdriver.Firefox(firefox_profile)
    # driver = webdriver.PhantomJS()
    return driver

if __name__ == '__main__':
    dr = browser()
    dr.get('http://www.baidu.com')
    dr.quit()