import pytest
import allure

from base_tests.base import BaseCase


class TestNegativeLogin(BaseCase):
    authorize = False

    @allure.feature('UI tests')
    @allure.story('Negative login')
    @allure.description("""Test login with wrong password""")
    @pytest.mark.UI
    def test_negativeLogin_with_redirection(self):
        not_logged = self.login_page.login_negative('di12kli@yandex.ru', '123456')
        assert not_logged and self.driver.current_url != self.login_page.url

    @allure.feature('UI tests')
    @allure.story('Negative login')
    @allure.description("""Test negative login with wrong name/password""")
    @pytest.mark.UI
    def test_negativeLogin_without_redirection(self):
        not_logged = self.login_page.login_negative('fffff','ffffff')
        assert not_logged and self.driver.current_url == self.login_page.url

class TestCreate(BaseCase):

    @allure.feature('UI tests')
    @allure.story('Create smth')
    @allure.description("""Test to create ad campaign""")
    @pytest.mark.UI
    def test_create_campaign(self, file_path):
        campaign = self.dash_page.go_to_campaign()
        campaign.create_campaign(file_path)

    @allure.feature('UI tests')
    @allure.story('Create smth')
    @allure.description("""Test to create segment""")
    @pytest.mark.UI
    def test_create_segment(self):
        segm = self.dash_page.go_to_segments()
        res = segm.createSeg()
        assert res[0]

class TestDelete(BaseCase):
    
    @allure.feature('UI tests')
    @allure.story('Delete smth')
    @allure.description("""Test to delete created segment""")
    @pytest.mark.UI
    def test_delete_segment(self):
        first_entry = self.dash_page.go_to_segments()
        first_entry.deleting()
