import pytest
from mysql.client import MysqlClient

@pytest.fixture(scope='session')
def mysql_client():
    mysql_client = MysqlClient(user='test_qa', password='qa_test', db_name='technoatom')
    mysql_client.connect()
    yield mysql_client
    mysql_client.connection.close()


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        mysql_client = MysqlClient(user='test_qa', password='qa_test', db_name='technoatom')
        mysql_client.recreate_db()
        mysql_client.connect()

        mysql_client.create_table('test_users')

        mysql_client.connection.close()


    