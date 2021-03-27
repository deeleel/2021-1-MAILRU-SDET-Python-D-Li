from base import BaseCase
import locators
import pytest

class Test(BaseCase):

    @pytest.mark.UI
    def test_authorize(self, login):
        assert 'https://target.my.com/dashboard' == self.driver.current_url

    @pytest.mark.UI
    def test_logout(self, login):
        self.click(locators.LOGOUT_ICON)
        self.click(locators.LOGOUT_LOCATOR)
        assert self.element_exist(locators.LOGIN_LOCATOR) == True

    @pytest.mark.UI
    def test_edit(self, login):
        self.click(locators.PROFILE_LOCATOR)
        res = self.edit_profile()
        assert res == True
    
    @pytest.mark.parametrize('locator, expected_loc',
        [
            (locators.PAGE1_LOCATOR, locators.SUCCESS1),
            (locators.PAGE2_LOCATOR, locators.SUCCESS2)
        ]    
    )
    @pytest.mark.UI
    def test_page(self, login, locator, expected_loc):
        self.click(locator)
        assert self.element_exist(expected_loc) == True

