from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import locators
import pytest
import time

CLICK_RETRY = 3

class BaseCase:
    driver = None
    config = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config):
        self.driver = driver
        self.config = config


    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                element = self.find(locator, timeout=timeout)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    @pytest.fixture(scope='function')
    def login(self):
        self.click(locators.LOGIN_LOCATOR)

        email = self.find(locators.LOGIN_EMAIL)
        email.send_keys('di12kli@yandex.ru')

        password = self.find(locators.LOGIN_PASSWORD)
        password.send_keys('simple123456')

        button = self.find(locators.LOGIN_BUTTON)
        button.click()

    def element_exist(self, locator):
        try:
            self.find(locator)
        except NoSuchElementException:
            return False
        return True
    
     def edit_profile(self):
        data = ['diana aleksandrovna', '79999999777', 'smth10@mail.ru']
        fio = self.find(locators.PROFILE_FIO)
        fio.clear()
        fio.send_keys(data[0])

        phone = self.find(locators.PROFILE_PHONE)
        phone.clear()
        phone.send_keys(data[1])

        email = self.find(locators.PROFILE_EMAIL)
        email.clear()
        email.send_keys(data[2])

        self.click(locators.PROFILE_SUBMIT)
        self.driver.refresh()

        fio = self.find(locators.PROFILE_FIO).get_attribute('value')
        phone = self.find(locators.PROFILE_PHONE).get_attribute('value')
        email = self.find(locators.PROFILE_EMAIL).get_attribute('value')

        return (False, True)[[fio, phone, email] == data]
