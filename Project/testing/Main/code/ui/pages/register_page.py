from ui.pages.base_page import BasePage
from ui.locators.pages_locators import RegistrationPageLocators
from ui.pages.dashboard_page import DashboardPage

import allure
import logging
logger = logging.getLogger('test')

class RegistrationPage(BasePage):
    
    url = 'http://notmyapp:8080/reg'
    locators = RegistrationPageLocators()

    @allure.step('Registering: name={name_inp}, password={passw_inp}, email={email_inp}')
    def register(self, name_inp, passw_inp, email_inp):
        user = self.find(self.locators.USERNAME_INPUT)
        user.send_keys(name_inp)

        passw = self.find(self.locators.PASSWORD_INPUT)
        passw.send_keys(passw_inp)

        confirm = self.find(self.locators.PASSWORD_REPEAT)
        confirm.send_keys(passw_inp)

        email = self.find(self.locators.EMAIL_INPUT)
        email.send_keys(email_inp)

        self.click(self.locators.ACCEPT_TERMS)
        self.click(self.locators.SUBMIT_BUTTON)

        logger.info('Submited valid data to register')
        return DashboardPage(self.driver)

    @allure.step('Registering: name={name_inp}, password={passw_inp}, email={email_inp} and checking error locator')
    def register_neg(self, name_inp, passw_inp, email_inp, error):
        user = self.find(self.locators.USERNAME_INPUT)
        user.send_keys(name_inp)

        passw = self.find(self.locators.PASSWORD_INPUT)
        passw.send_keys(passw_inp)

        confirm = self.find(self.locators.PASSWORD_REPEAT)
        confirm.send_keys(passw_inp)

        email = self.find(self.locators.EMAIL_INPUT)
        email.send_keys(email_inp)

        self.click(self.locators.ACCEPT_TERMS)
        self.click(self.locators.SUBMIT_BUTTON)

        logger.info('Submited invalid data to register')
        if error:
            return self.element_exist(self.locators.ALERT)
        else:
            return self.driver.current_url == self.url


    @allure.step('Registering: name={name_inp}, password={passw_inp}, email={email_inp} and checking error locator')
    def wrong_register_message(self, name_inp, passw_inp, email_inp, mssg):
        self.register_neg(name_inp, passw_inp, email_inp, mssg)

        if mssg is not None:
            flash = (self.locators.ALERT_AD[0], self.locators.ALERT_AD[1].format(mssg))
            return self.element_exist(flash)
        else:
            return True

            