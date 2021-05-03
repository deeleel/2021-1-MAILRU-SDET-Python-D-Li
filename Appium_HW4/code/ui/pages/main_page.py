from ui.pages.base_page import BasePage
from ui.pages.settings_page import SettingsPageANDROID
from ui.locators.locators_android import MainPageANDROIDLocators
import allure


class MainPageANDROID(BasePage):
    locators = MainPageANDROIDLocators()

    @allure.step('Clicking on keyboard')
    def click_on_keyboard(self):
        self.click_for_android(self.locators.KEYBOARD_BUTTON)

    @allure.step('Send text: {text}')
    def input_request(self, text):
        if self.element_exist(self.locators.KEYBOARD_INPUT):
            self.find(self.locators.KEYBOARD_INPUT).send_keys(text)

    @allure.step('Sending question')
    def send_request(self):
        self.click_for_android(self.locators.INPUT_BUTTON)

    def my_request(self, text):
        self.click_on_keyboard()
        self.input_request(text)
        self.send_request()
        self.driver.hide_keyboard()

    @allure.step('Checking response')
    def check_answer_contains(self, text):
        assert self.element_exist((self.locators.CARD_CONTAINS[0], self.locators.CARD_CONTAINS[1].format(text)))

    @allure.step('Checking response')
    def check_answer(self, text):
        assert self.element_exist((self.locators.MESSAGE[0], self.locators.MESSAGE[1].format(text)))

    @allure.step('Checking response')
    def check_track(self, name):
        assert self.element_exist((self.locators.TRACK_NAME[0], self.locators.TRACK_NAME[1].format(name)))

    @allure.step('Scrolling to {name}')
    def scrolling_suggestions_to_element(self, name):
        while not self.element_exist((self.locators.SUGGEST_ITEM[0], self.locators.SUGGEST_ITEM[1].format(name))):
            self.swipe_element_to_left(self.locators.SUGGEST_LIST)
        self.click_for_android((self.locators.SUGGEST_ITEM[0], self.locators.SUGGEST_ITEM[1].format(name)))

    @allure.step('Choose news')
    def choose_news(self, name):
        self.click_for_android(self.locators.BURGER_MENU)
        return SettingsPageANDROID(self.driver, self.config).choose_news_origin(name)

    @allure.step('Checking news track')
    def check_news_track(self, req, res):
        self.my_request(req)
        self.check_track(res)

    @allure.step('Check app info')
    def check_info(self, app_version, text):
        self.click_for_android(self.locators.BURGER_MENU)
        return SettingsPageANDROID(self.driver, self.config).choose_settings_about(app_version, text)
        

