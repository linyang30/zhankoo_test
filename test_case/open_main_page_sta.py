import unittest

from test_case.models.myunit import MyTest
from test_case.page_obj.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
import time
import random
from selenium.webdriver.support.select import Select
import win32con
import win32gui
from test_case.driver import driver


class OpenMainPageTest(MyTest):
    '''打开展酷首页'''
    def setUp(self):
        self.browser = driver.browser()


    def _test_open_main_page(self):
        '''打开展酷首页'''
        MainPage(self.driver).open_mainpage()

    def _test5(self):
        datas = self.excel_table_by_index()
        for data in datas:
            self.browser.get("http://www.zhankoo.com")
            loginElem = WebDriverWait(self.browser, 10).until(
                lambda x: x.find_element_by_xpath('//*[@id="pg"]/div/ul/li[2]/a[2]'))
            loginElem.click()
            nameElem = WebDriverWait(self.browser, 10).until(
                lambda x: x.find_element_by_xpath('//*[@id="Name"]'))
            nameElem.send_keys(str(int(data[0])))
            passElem = WebDriverWait(self.browser, 10).until(
                lambda x: x.find_element_by_xpath('//*[@id="Password"]'))
            try:
                pwd = str(int(data[1]))
            except:
                pwd = str(data[1])
            passElem.send_keys(pwd)
            loginButtonElem = self.browser.find_element_by_xpath('//*[@id="js-login"]')
            loginButtonElem.click()
            resTextElem = WebDriverWait(self.browser, 20).until(
                lambda x: x.find_element_by_xpath('//*[@id="pg"]/div/ul/li[2]/a[1]/em'))
            assert resTextElem.text == data[2]
            logoutElem = WebDriverWait(self.browser, 10).until(
                lambda x: x.find_element_by_xpath('//*[@id="pg"]/div/ul/li[2]/a[2]'))
            logoutElem.click()

    def test6(self):
        '''
        主办方登陆并发布展会
        '''
        # self.browser.implicitly_wait(10)
        self.browser.get("http://www.zhankoo.com/") #打开展酷首页
        loginElem = WebDriverWait(self.browser, 10).until(
            lambda x: x.find_element_by_xpath('//*[@id="pg"]/div/ul/li[2]/a[2]')) #寻找登录按钮
        loginElem.click() #点击登录按钮
        time.sleep(1)
        nameElem = WebDriverWait(self.browser, 10).until(
            lambda x: x.find_element_by_xpath('//*[@id="Name"]')) #寻找登录名称控件
        nameElem.send_keys('18320836325') #输入登陆名称
        #time.sleep(5)
        passElem = WebDriverWait(self.browser, 10).until(
            lambda x: x.find_element_by_xpath('//input[@id="Password"]')) #寻找登录密码控件
        passElem.send_keys('123456') #输入登陆密码
        #time.sleep(5)
        loginButtonElem = WebDriverWait(self.browser, 10).until(lambda x: x.find_element_by_xpath('//*[@id="js-login"]')) #寻找登录按钮
        loginButtonElem.click() #点击登录按钮
        resTextElem = WebDriverWait(self.browser, 20).until(
            lambda x: x.find_element_by_xpath('//*[@id="pg"]/div/ul/li[2]/a[1]/em'))
        assert resTextElem.text == '主办方' # 判断登陆的用户是否是主办方
        # currentWindow = self.browser.current_window_handle
        # backElem = WebDriverWait(self.browser, 10).until(
        #     lambda x: x.find_element_by_xpath('//*[@id="pg"]/div/ul/li[2]/a[1]')) # 寻找进入主办方后台按钮
        # backElem.click() #点击进入主办方后台
        # #time.sleep(5)
        # handles = self.browser.window_handles
        # for handle in handles:
        #     if handle != currentWindow:
        #         self.browser.switch_to.window(handle)
        # releaseExhibitionElem = WebDriverWait(self.browser, 10).until(
        #     lambda x: x.find_element_by_xpath('//*[@id="menu"]/ul[1]/li[2]/a')) #寻找发布展会按钮
        # releaseExhibitionElem.click() #点击发布展会按钮
        # #time.sleep(5)
        # exhibitionEditButtonElem = WebDriverWait(self.browser, 10).until(lambda x: x.find_element_by_xpath('//*[@id="BtnBasic"]')) #寻找编辑展会按钮
        # exhibitionEditButtonElem.click() #点击编辑展会按钮
        # #time.sleep(5)
        # exhibitionNameElem = WebDriverWait(self.browser, 10).until(lambda x: x.find_element_by_xpath('//*[@id="Name"]')) #寻找展会名称控件
        # exhibitionNameElem.send_keys('Test' + str(random.randint(1, 100000))) #填写展会名称
        # #time.sleep(5)
        # exhibitionShortNameElem = WebDriverWait(self.browser, 10).until(lambda x: x.find_element_by_xpath('//*[@id="ShortName"]')) #寻找展会简称控件
        # exhibitionShortNameElem.send_keys('Test') #填写展会简称
        # #time.sleep(5)
        # Select(self.browser.find_element_by_xpath('//*[@id="IndustryID"]')).select_by_value('1') #选择展会分类
        # #time.sleep(5)
        #
        # #exhibitionIndustryTypeElem = WebDriverWait(self.browser, 10).until(lambda x: x.find_element_by_xpath('//*[@id="60"]')) #寻找展会分类中的第一个
        # exhibitionIndustryTypeElem = self.browser.find_element_by_id('sonIndustryTypes').find_element_by_id('3')
        # exhibitionIndustryTypeElem.click() #点击展品分类的第一个
        #
        # #time.sleep(5)
        # # exhibitionFrequencyWithYearElem = WebDriverWait(self.browser, 10).until(lambda x: x.find_element_by_xpath('//*[@id="HoldFrequencyWithYear"]')) #寻找举办频次年的控件
        # # exhibitionFrequencyWithYearElem.send_keys('1') #填写举办频次年
        # # time.sleep(5)
        # # exhibitionFrequencyElem = WebDriverWait(self.browser, 10).until(lambda x: x.find_element_by_xpath('//*[@id="HoldFrequency"]')) #寻找举办频次届的控件
        # # exhibitionFrequencyElem.send_keys('1') #填写举办频次届
        # # time.sleep(5)
        # datePickerStartJS = "$('input[id=FromOn]').attr('value','2017/01/01')"
        # datePickerEndJS = "$('input[id=ToOn]').attr('value','2017/01/05')"
        # self.browser.execute_script(datePickerStartJS) #填写展会开始时间
        # #time.sleep(5)
        # self.browser.execute_script(datePickerEndJS) #填写展会结束时间
        # #time.sleep(5)
        # selectPavilionElem = WebDriverWait(self.browser, 10).until(lambda x: x.find_element_by_xpath('//*[@id="DivBasic"]/table/tbody/tr[6]/td[2]/button')) #寻找展馆选择框按钮
        # selectPavilionElem.click() #点击展馆选择框按钮
        # time.sleep(1)
        #
        # self.browser.switch_to.frame('layui-layer-iframe1')
        #
        # pavilionElem = WebDriverWait(self.browser, 10).until(lambda x: x.find_element_by_xpath('//*[@id="PavilionPaged"]/div[1]/ul/li[1]/input')) #寻找第一个展馆控件
        # pavilionElem.click() #点击第一个展馆
        # #time.sleep(1)
        # #pavilionJS = "$('input[name=PavilionId]').attr('value','3507')"
        # #self.browser.execute_script(pavilionJS)
        # selectPavilionButtonElem = WebDriverWait(self.browser, 10).until(lambda x: x.find_element_by_xpath('//*[@id="SelectPavilion"]')) #寻找确定按钮按钮
        # selectPavilionButtonElem.click() #点击确定按钮
        # #time.sleep(1)
        # saveButtonElem = WebDriverWait(self.browser, 10).until(lambda x: x.find_element_by_xpath('//*[@id="DivBasic"]/div/button[1]')) #寻找保存按钮
        # saveButtonElem.click() #点击保存按钮
        # time.sleep(1)
        #
        #
        # addPicButtonElem = WebDriverWait(self.browser, 10).until(lambda x: x.find_element_by_xpath('//*[@id="BtnPicture"]'))
        # addPicButtonElem.click()
        # time.sleep(1)
        # #picUploadElem = WebDriverWait(self.browser, 10).until(lambda x: x.find_element_by_xpath('//*[@id="FileUpload1"]'))
        # #picUploadElem.send_keys("D:\\Temp\\1.jpg")
        # picUploadElems = self.browser.find_elements_by_id('FileUpload1')
        # print(len(picUploadElems))
        # for picUpload in picUploadElems:
        #     picUpload.click()
        #     time.sleep(1)
        #     uploadwindow = win32gui.FindWindow('#32770', '打开')
        #     parent = win32gui.FindWindowEx(uploadwindow, None, 'ComboBoxEx32', None)
        #     Combobox_real = win32gui.FindWindowEx(parent, None, 'ComboBox', None)
        #     Edit_box = win32gui.FindWindowEx(Combobox_real, None, 'Edit', None)
        #     button = win32gui.FindWindowEx(uploadwindow, None, 'Button', None)
        #     win32gui.SendMessage(Edit_box, win32con.WM_SETTEXT, None, 'D:\\Temp\\1.jpg')
        #     win32gui.SendMessage(uploadwindow, win32con.WM_COMMAND, 1, button)
        #     time.sleep(1)
        # savePicButtonElem = WebDriverWait(self.browser, 10).until(lambda x: x.find_element_by_xpath('//*[@id="DivPicture"]/div[3]/button[1]'))
        # savePicButtonElem.click()
        # time.sleep(1)







if __name__ == '__main__':
    unittest.main()