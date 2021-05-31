import pytest
from utils.builder import Builder

class ApiBase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client):
        self.api_client = api_client
        self.builder = Builder