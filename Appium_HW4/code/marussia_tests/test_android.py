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
        self.main_page.choose_news('Вести FM')
        self.main_page.go_back()
        self.main_page.check_news_track('News', 'Вести ФМ')


@allure.story('Взаимодействие с настройками приложения')
class TestSettings(BaseCase):

    @allure.description("""Проверка корректности настроек приложения""")
    @pytest.mark.AndroidUI
    def test_settings(self, app_version):
        self.main_page.check_info(app_version, 'Все права защищены')
