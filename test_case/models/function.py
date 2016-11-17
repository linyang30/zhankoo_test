import os
from selenium import webdriver

def insert_img(driver, filename):
    base_dir = os.getcwd()
    base = base_dir.split('\\test_case')[0]
    file_path = base + '\\report\\image\\' + filename
    driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    insert_img(driver, 'baidu.jpg')
    driver.quit()