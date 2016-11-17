from test_case.page_obj.base import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    '''展酷首页'''
    url = '/'

    #打开首页
    def open_mainpage(self):
        self.open()
