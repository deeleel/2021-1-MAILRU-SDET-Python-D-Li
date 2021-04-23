from ui.pages.base_page import BasePage
from ui.locators.locators_android import SettingsPageANDROIDLocators
import allure


class SettingsPage(BasePage):
    locators = None

    @allure.step('Go to news settings')
    def choose_news_origin(self):
        pass

    @allure.step('Go to about settings')
    def choose_settings_about(self):
        pass


class SettingsPageANDROID(SettingsPage):
    locators = SettingsPageANDROIDLocators()

    @allure.step('Go to news settings')
    def choose_news_origin(self):
        self.swipe_to_element(self.locators.NEWS_BUTTON, 1)
        self.click_for_android(self.locators.NEWS_BUTTON)

    @allure.step('Go to about settings')
    def choose_settings_about(self):
        self.swipe_to_element(self.locators.ABOUT_PROGRAM_BUTTON, 2)
        self.click_for_android(self.locators.ABOUT_PROGRAM_BUTTON)