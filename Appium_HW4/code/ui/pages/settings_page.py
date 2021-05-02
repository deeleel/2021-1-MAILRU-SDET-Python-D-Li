from ui.pages.base_page import BasePage
from ui.pages.news_page import NewsPageANDROID
from ui.pages.about_page import AboutPageANDROID
from ui.locators.locators_android import SettingsPageANDROIDLocators
import allure


class SettingsPageANDROID(BasePage):
    locators = SettingsPageANDROIDLocators()

    @allure.step('Go to news settings')
    def choose_news_origin(self, name):
        self.swipe_to_element(self.locators.NEWS_BUTTON, 1)
        self.click_for_android(self.locators.NEWS_BUTTON)
        return NewsPageANDROID(self.driver, self.config).set_news_origin(name)

    @allure.step('Go to about settings')
    def choose_settings_about(self, app_version, text):
        self.swipe_to_element(self.locators.ABOUT_PROGRAM_BUTTON, 2)
        self.click_for_android(self.locators.ABOUT_PROGRAM_BUTTON)
        return AboutPageANDROID(self.driver, self.config).check_settings_about(app_version, text)