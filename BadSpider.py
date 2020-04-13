import time

from usercode.AbstractSpider import AbstractSpider


class BadSpider(AbstractSpider):
    def execute(self):
        self.wait_for_element_loading((self.located_by.ID, 'com.baidu.searchbox:id/eq'), 10)
        time.sleep(15)
        raise AttributeError("I'm bad!")
