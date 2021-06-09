import pytest
from _pytest.fixtures import FixtureRequest
from utils.builder import Builder

from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage

    
class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest, api_client, logger, ui_report):
        self.driver = driver
        self.config = config
        self.logger = logger

        self.builder = Builder()
        self.api_client = api_client

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.login_page: LoginPage = request.getfixturevalue('login_page')

        self.logger.info('Initial setup done!')
