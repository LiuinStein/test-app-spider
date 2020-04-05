from abc import abstractmethod, ABCMeta

from appium import webdriver
from appium.webdriver.common import mobileby
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from persistence.AbstractPersistence import AbstractPersistence


class AbstractSpider(metaclass=ABCMeta):
    def __init__(self, driver, dao):
        if not isinstance(driver, webdriver.Remote) or not isinstance(dao, AbstractPersistence):
            raise TypeError("Check if the type of driver or dao object match its proper type during constructing "
                            "AbstractSpider.")
        self.driver = driver
        self.dao = dao
        self.located_by = mobileby.MobileBy()

    def wait_for_element_loading(self, locator, timeout):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator=locator))

    def click_element_by_id(self, identifier):
        self.driver.find_element_by_id(identifier).click()

    @abstractmethod
    def execute(self):
        pass
