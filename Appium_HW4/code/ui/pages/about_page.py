from ui.pages.base_page import BasePage
from ui.locators.locators_android import AboutPageANDROIDLocators
import allure


class AboutPage(BasePage):
    locators = None

    @allure.step("Checking settings: version = {version} and footer contains {text}")
    def check_settings_about(self, version, text):
        pass


class AboutPageANDROID(AboutPage):
    locators = AboutPageANDROIDLocators()

    @allure.step("Checking settings: version = {version} and footer contains {text}")
    def check_settings_about(self, version='1.39.1', text='Все права защищены'):
        assert self.element_exist((self.locators.VERSION[0], self.locators.VERSION[1].format(version)))
        assert self.element_exist((self.locators.COPYRIGHT[0], self.locators.COPYRIGHT[1].format(text)))