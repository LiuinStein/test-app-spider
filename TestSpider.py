from usercode.AbstractSpider import AbstractSpider


class TestSpider(AbstractSpider):
    def execute(self):
        self.wait_for_element_loading((self.located_by.ID, 'com.baidu.searchbox:id/eq'), 10)
        self.click_element_by_id('com.baidu.searchbox:id/eq')
