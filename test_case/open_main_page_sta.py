from test_case.models.myunit import MyTest
from test_case.page_obj.main_page import MainPage
import unittest

class OpenMainPageTest(MyTest):
    '''打开展酷首页'''


    def test_open_main_page(self):
        '''打开展酷首页'''
        MainPage(self.driver).open_mainpage()







if __name__ == '__main__':
    unittest.main()