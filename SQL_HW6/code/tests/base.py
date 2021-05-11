from mysql.builder import MySQLBuilder
import pytest


class MySQLBase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client, get_data):

        self.mysql = mysql_client
        self.mysql_builder = MySQLBuilder(mysql_client)

        self.data = get_data