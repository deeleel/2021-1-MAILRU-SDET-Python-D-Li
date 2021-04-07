from ui.pages.base_page import BasePage, PageNotLoadedException
from ui.locators.pages_locators import LoginPageLocators

from ui.pages.dashboard_page import DashboardPage
import allure

class LoginPage(BasePage):
    locators = LoginPageLocators()

    @allure.step('Logging in and going to dashboard if we are successfully logged')
    def login(self, login_inp, password_inp):
        self.click(self.locators.LOGIN_LOCATOR)

        email = self.find(self.locators.LOGIN_EMAIL)
        email.send_keys(login_inp)

        password = self.find(self.locators.LOGIN_PASSWORD)
        password.send_keys(password_inp)

        self.click(self.locators.LOGIN_BUTTON)

        if self.element_exist(self.locators.NEGATIVE_LOGIN_NAME) or self.element_exist(self.locators.NEGATIVE_LOGIN_NAME2):
            return False
        else:
            return DashboardPage(self.driver)

    