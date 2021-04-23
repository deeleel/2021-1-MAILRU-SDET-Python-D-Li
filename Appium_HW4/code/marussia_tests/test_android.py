import time
import allure
import pytest
from marussia_tests.base import BaseCase


@allure.story('Взаимодействие с окном команд')
class TestMainPage(BaseCase):

    @allure.description("""Проверка корректности поисковой выдачи""")
    @pytest.mark.AndroidUI
    def test_request(self):
        text = 'Территория России в её конституционных границах составляет 17 125 191'
        self.main_page.my_request('Russia')
        self.main_page.check_answer_contains(text)

        self.main_page.scrolling_suggestions_to_element('численность населения россии')
        self.main_page.check_answer_contains('146 млн.')


@allure.story('Взаимодействие с окном команд, функционал "Калькулятор"')
class TestCalculator(BaseCase):

    @allure.description("""Проверка простого математического выражения""")
    @pytest.mark.AndroidUI
    def test_simple_math(self):
        self.main_page.my_request('5*2*1')
        self.main_page.check_answer('10')


@allure.story('Взаимодействие с источником новостей')
class TestNews(BaseCase):

    @allure.description("""Проверка корректности выбора новостей""")
    @pytest.mark.AndroidUI
    def test_news_origin(self):
        self.main_page.click_for_android(self.main_page.locators.BURGER_MENU)
        self.settings_page.choose_news_origin()
        self.news_page.set_news_origin('Вести FM')

        self.driver.back()
        self.driver.back()

        self.main_page.my_request('News')
        self.main_page.check_track('Вести ФМ')


@allure.story('Взаимодействие с настройками приложения')
class TestSettings(BaseCase):

    @allure.description("""Проверка корректности настроек приложения""")
    @pytest.mark.AndroidUI
    def test_settings(self):
        self.main_page.click_for_android(self.main_page.locators.BURGER_MENU)
        self.settings_page.choose_settings_about()
        self.about_page.check_settings_about()





