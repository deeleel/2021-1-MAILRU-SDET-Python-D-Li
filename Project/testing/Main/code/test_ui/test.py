import pytest
import allure
from urllib.parse import urljoin

from test_ui.base import BaseCase
from utils.test_data import LOGIN_DATA, REGISTER_DATA, NAV_DATA, LINK_DATA, CIRCLE_DATA, DEFAULT_USER





class TestLogin(BaseCase):

    @pytest.mark.UI
    @allure.feature('Test valid Login')
    @allure.story('Successfully logging in')
    @allure.description(
        """ Logging in 
            1. Creating user via api
            2. Logging that user in
            3. Expecting Page with title opened: Test Server | Welcome!
            4. Deleting created user
        """)  
    def test_valid_login(self):
        cred = self.api_client.create_user()
        self.login_page.login(cred['name'], cred['password'])

        assert self.driver.title == 'Test Server | Welcome!', 'Main page not opened'
        self.api_client.delete_api_user(cred['name'], from_ui=True)

    
    @pytest.mark.UI
    @allure.feature('Test invalid Login')
    @allure.story('Try to log in with invalid data')
    @allure.description(
        """ Logging in with invalid data
            1. Logging in using method for wrong logging
            2. Expecting that logging return True, meaning we are not logged
        """) 
    @pytest.mark.parametrize('name, passw, mssg', LOGIN_DATA)
    def test_invalid_login(self, name, passw, mssg):
        not_logged = self.login_page.login_negative(name, passw, mssg)
        assert not_logged, 'Wrong user is logged'


    @pytest.mark.UI
    @allure.feature('Test invalid Login')
    @allure.story('Checking message of log in with invalid data')
    @allure.description(
        """ Logging in with invalid data
            1. Logging in using method for wrong logging
            2. Expecting that 
        """) 
    @pytest.mark.parametrize('name, passw, mssg', LOGIN_DATA)
    def test_invalid_login_message(self, name, passw, mssg):
        valid_message = self.login_page.login_negative_message(name, passw, mssg)
        assert valid_message, 'Message is Wrong'



class TestLogout(BaseCase):


    @pytest.mark.UI
    @allure.feature('Test Logout')
    @allure.story('Logging out')
    @allure.description(
        """ Logging user out
            1. Creating user via api
            2. Logging that user in
            3. Logging out that user
            4. Expecting that we are redirected to /login page
            5. Deleting created user
        """)
    def test_logout(self):
        cred = self.api_client.create_user()
        dash_page = self.login_page.login(cred['name'], cred['password'])
        dash_page.logout()
        
        assert self.driver.current_url == urljoin(self.base_page.url, '/login'), 'Not redirected to login page'
        self.api_client.delete_api_user(cred['name'], from_ui=True)



class TestRegistration(BaseCase):


    @pytest.mark.UI
    @allure.feature('Test valid Registration')
    @allure.story('Test register user')
    @allure.description(
        """ Registering user
            1. From login_page going to registration_page
            2. Registering user with valid data
            3. Expecting welcome page is opened
            4. Deleting created user
        """)
    def test_register(self):
        reg_page = self.login_page.go_to_reg()
        name = self.builder.name()
        passw = self.builder.passw()
        email = self.builder.email()

        reg_page.register(name, passw, email)
        assert self.driver.title == 'Test Server | Welcome!', 'Main page not opened'
        self.api_client.delete_api_user(name, from_ui=True)


    @pytest.mark.UI
    @allure.feature('Test invalid Registration')
    @allure.story('Test register user with invalid user')
    @allure.description(
        """ Registering invalid user
            1. From login_page going to registration_page
            2. Registering user with invalid data and method for wrong registration
            3. Expecting that method return True, user not registered 
        """)
    @pytest.mark.parametrize('name, passw, email, mssg', REGISTER_DATA)
    def test_wrong_register(self, name, passw, email, mssg):
        reg_page = self.login_page.go_to_reg()
        not_regged = reg_page.register_neg(name, passw, email, mssg)
        assert not_regged, 'Wrong user was added'


    @pytest.mark.UI
    @allure.feature('Test Registration message')
    @allure.story('Check message of invalid user')
    @allure.description(
        """ Registering invalid user
            1. From login_page going to registration_page
            2. Registering user with invalid data and method for wrong registration
            3. Expecting that method return True, user not registered 
        """)
    @pytest.mark.parametrize('name, passw, email, mssg', REGISTER_DATA)
    def test_wrong_register_message(self, name, passw, email, mssg):
        reg_page = self.login_page.go_to_reg()
        valid_message = reg_page.wrong_register_message(name, passw, email, mssg)
        assert valid_message, 'Wrong message'



class TestNav(BaseCase):
    
    @pytest.mark.UI
    @allure.feature('Test main Navbar')
    @allure.story('Test main navbar buttons')
    @allure.description(
        """ Clicking on navbar main buttons
            1. Creating user
            2. Logging in that user
            3. Clicking on nav button
            4. Expecting that current url is expected
            5. Deleting created user
        """)
    @pytest.mark.parametrize('nav, expected_res', NAV_DATA)
    def test_navbar(self, nav, expected_res):
        cred = self.api_client.create_user()
        dash_page = self.login_page.login(cred['name'], cred['password'])
        dash_page.click_nav(nav)

        assert self.driver.current_url == expected_res, 'Url is not expected'
        self.api_client.delete_api_user(cred['name'], from_ui=True)


    @pytest.mark.UI
    @allure.feature('Test Navbar links')
    @allure.story('Test main navbar links')
    @allure.description(
        """ Clicking on navbar dropdown links
            1. Creating user
            2. Logging in that user
            3. Clicking on nav link
            4. Expecting that new tab is opened
            5. Going to new tab
            6. Expecting that current url is expected
            7. Deleting created user
        """)
    @pytest.mark.parametrize('nav, link, expected_url', LINK_DATA)
    def test_links(self, nav, link, expected_url):
        cred = self.api_client.create_user()
        dash_page = self.login_page.login(cred['name'], cred['password'])

        dash_page.click_link(nav, link)

        assert len(self.driver.window_handles) == 2, 'New tab is not opened'
        dash_page.change_tab()
        assert self.driver.current_url == expected_url, 'Url is not expected'
        self.api_client.delete_api_user(cred['name'], from_ui=True)



class TestMainContent(BaseCase):

    @pytest.mark.UI
    @allure.feature('Test Circle')
    @allure.story('Test main circles')
    @allure.description(
        """ Clicking on navbar main buttons
            1. Creating user
            2. Logging in that user
            3. Clicking on main circle
            4. Expecting that new tab is opened
            5. Going to new tab
            6. Expecting that current url is expected
            7. Deleting created user
        """)
    @pytest.mark.parametrize('name, expected_url', CIRCLE_DATA)
    def test_circle(self, name, expected_url):
        cred = self.api_client.create_user()
        dash_page = self.login_page.login(cred['name'], cred['password'])
        dash_page.click_circle(name)

        assert len(self.driver.window_handles) == 2, 'New tab is not opened'
        dash_page.change_tab()
        assert self.driver.current_url == expected_url, 'Url is not expected'
        self.api_client.delete_api_user(cred['name'], from_ui=True)


    @pytest.mark.UI
    @allure.feature('Test Quotes')
    @allure.story('Test main quotes')
    @allure.description(
        """ Clicking on navbar main buttons
            1. Creating user
            2. Logging in that user
            3. Remember current quote
            4. Refreshing page
            6. Expecting that current quote is not remembered one
            7. Deleting created user
        """)
    def test_quotes(self):
        cred = self.api_client.create_user()
        dash_page = self.login_page.login(cred['name'], cred['password'])

        text = dash_page.get_quote()
        self.driver.refresh()
        text2 = dash_page.get_quote()

        assert text != text2, 'Text not changed'
        self.api_client.delete_api_user(cred['name'], from_ui=True)


   
class TestName(BaseCase):

    @pytest.mark.UI 
    @allure.feature('Test nav name')
    @allure.story('Test name')
    @allure.description(
        """ Clicking on navbar main buttons
            1. Creating user
            2. Logging in that user
            6. Expecting that current name is user's name
            7. Deleting created user
        """)
    def test_nav_name(self):
        cred = self.api_client.create_user()
        dash_page = self.login_page.login(cred['name'], cred['password'])

        assert dash_page.check_name(cred['name']), 'Name is not here'
        self.api_client.delete_api_user(cred['name'], from_ui=True)



 
class TestMock(BaseCase):
    

    @pytest.mark.UI 
    @allure.feature('Test Mock')
    @allure.story('Test Mock id not visible')
    @allure.description(
        """ Checking id is not visible
            1. Logging in new user
            2. Expecting that VK_ID is not visible
            3. Deleting new user
        """)
    def test_mock_id(self):
        cred = self.api_client.create_user()
        dash_page = self.login_page.login(cred['name'], cred['password'])

        assert not dash_page.check_id(), 'There is VK_ID'
        self.api_client.delete_api_user(cred['name'], from_ui=True)




