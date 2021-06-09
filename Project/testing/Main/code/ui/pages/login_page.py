from ui.pages.base_page import BasePage
from ui.locators.pages_locators import LoginPageLocators
from ui.pages.dashboard_page import DashboardPage
from ui.pages.register_page import RegistrationPage

import allure
import logging
logger = logging.getLogger('test')


class LoginPage(BasePage):
    url = 'http://notmyapp:8080/'
    locators = LoginPageLocators()

    @allure.step('Logging in with wrong data')
    def login_negative(self, login_inp, password_inp, mssg):
        name = self.find(self.locators.USERNAME_INPUT)
        name.send_keys(login_inp)

        password = self.find(self.locators.PASSWORD_INPUT)
        password.send_keys(password_inp)

        self.click(self.locators.SUBMIT_BUTTON)
        logger.info('Submited wrong login')

        if mssg:
            return self.element_exist(self.locators.ALERT)
        else:
            return self.driver.current_url == self.url


    @allure.step('Logging in with wrong data and checking error message')
    def login_negative_message(self, login_inp, password_inp, mssg):
        self.login_negative(login_inp, password_inp, mssg)
        if mssg is not None:
            flash = (self.locators.ALERT_AD[0], self.locators.ALERT_AD[1].format(mssg))
            return self.element_exist(flash)
        else:
            return True
    

    @allure.step('Successfully logging in')
    def login(self, login_inp='deelee', password_inp='111111'):

        name = self.find(self.locators.USERNAME_INPUT)
        name.send_keys(login_inp)

        password = self.find(self.locators.PASSWORD_INPUT)
        password.send_keys(password_inp)

        self.click(self.locators.SUBMIT_BUTTON)
        logger.info('Submited valid login')
        return DashboardPage(self.driver)

    @allure.step('Clicking to register')
    def go_to_reg(self):
        self.click(self.locators.CREATE_ACC)
        logger.info('Going to Register page from login')
        return RegistrationPage(self.driver)
