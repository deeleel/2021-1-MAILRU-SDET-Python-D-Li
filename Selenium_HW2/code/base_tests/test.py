import pytest
import allure

from base_tests.base import BaseCase


class TestNegative(BaseCase):
    authorize = False

    @allure.feature('UI tests')
    @allure.story('Negative login')
    @allure.description("""Test login with wrong password""")
    @pytest.mark.UI
    def test_1(self):
        logged = self.login_page.login('di12kli@yandex.ru', '123456')
        assert not logged and self.driver.current_url != self.login_page.url

    @allure.feature('UI tests')
    @allure.story('Negative login')
    @allure.description("""Test negative login with wrong name/password""")
    @pytest.mark.UI
    def test_2(self):
        logged = self.login_page.login('fffff','ffffff')
        assert not logged and self.driver.current_url == self.login_page.url

class TestCreate(BaseCase):

    @allure.feature('UI tests')
    @allure.story('Create smth')
    @allure.description("""Test to create ad campaign""")
    @pytest.mark.UI
    def test_one(self, file_path):
        campaign = self.dash_page.go_to_campaign()
        campaign.create_campaign(file_path)

    @allure.feature('UI tests')
    @allure.story('Create smth')
    @allure.description("""Test to create segment""")
    @pytest.mark.UI
    def test(self):
        segm = self.dash_page.go_to_segments()
        segm.createSeg()

class TestDelete(BaseCase):
    
    @allure.feature('UI tests')
    @allure.story('Delete smth')
    @allure.description("""Test to delete existing segment""")
    @pytest.mark.UI
    def test(self):
        first_entry = self.dash_page.go_to_segments()
        first_entry.deleting()
