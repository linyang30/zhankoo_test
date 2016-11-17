class Page:

    url = 'http://www.zhankoo.com'

    def __init__(self, selenium_driver, base_url = url):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30

