import pytest
from utils.builder import Builder


class ApiBase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client, mock_client, logger):
        self.builder = Builder()
        self.logger = logger

        self.api_client = api_client
        self.mock_client = mock_client

        self.logger.info('Initial setup done!')

