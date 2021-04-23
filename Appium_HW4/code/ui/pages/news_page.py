from ui.pages.base_page import BasePage
from ui.locators.locators_android import NewsPageANDROIDLocators
import allure


class NewsPage(BasePage):
    locators = None

    @allure.step('Choosing news')
    def set_news_origin(self, name):
        pass


class NewsPageANDROID(NewsPage):
    locators = NewsPageANDROIDLocators()

    @allure.step('Choosing news')
    def set_news_origin(self, name):
        self.click_for_android((self.locators.CHOOSE_NEWS[0], self.locators.CHOOSE_NEWS[1].format(name)))
        assert self.element_exist((self.locators.SELECTED_ITEM[0], self.locators.SELECTED_ITEM[1].format(name)))