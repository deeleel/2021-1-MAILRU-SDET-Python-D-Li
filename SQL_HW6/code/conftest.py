import pytest

from stuff.data import read_data
from mysql.client import MysqlClient

@pytest.fixture(scope='session')
def mysql_client():
    mysql_client = MysqlClient(user='root', password='pass', db_name='TEST_SQL')
    mysql_client.connect()
    yield mysql_client
    mysql_client.connection.close()


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        mysql_client = MysqlClient(user='root', password='pass', db_name='TEST_SQL')
        mysql_client.recreate_db()

        mysql_client.connect()

        mysql_client.create_table('requests')
        mysql_client.create_table('requestTypes')
        mysql_client.create_table('popularRequests')
        mysql_client.create_table('err4Requests')
        mysql_client.create_table('err5Requests')

        mysql_client.connection.close()


@pytest.fixture(scope='session')
def get_data():
    return read_data()
    