from selenium.webdriver.common.keys import Keys
from base import BaseCase
import locators
import pytest
import time

class Test(BaseCase):

    @pytest.mark.UI
    def test_authorize(self, login):
        assert 'https://target.my.com/dashboard' == self.driver.current_url

    @pytest.mark.UI
    def test_logout(self, login):
        self.click(locators.LOGOUT_ICON)
        self.click(locators.LOGOUT_LOCATOR)
        time.sleep(3)
        assert 'Войти' in self.driver.page_source

    @pytest.mark.UI
    def test_edit(self, login):
        data = ['diana l', '79999999777', 'smth10@mail.ru']
        self.click(locators.PROFILE_LOCATOR)

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

        assert [fio, phone, email] == data
    
    @pytest.mark.parametrize('locator, expected_res',
        [
            (locators.PAGE1_LOCATOR, 'Конструктор отчётов'),
            (locators.PAGE2_LOCATOR, 'Аудиторные сегменты')
        ]    
    )
    @pytest.mark.UI
    def test_page(self, login, locator, expected_res):
        self.click(locator)
        time.sleep(3)
        assert expected_res in self.driver.page_source

time.sleep(5)
