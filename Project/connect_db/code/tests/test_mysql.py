from tests.base import MySQLBase
from mysql.models import Users
from default_user import DEFAULT_USER

class TestDB(MySQLBase):

    def test_add_user(self):
        self.mysql_builder.fill_user(DEFAULT_USER['name'], DEFAULT_USER['password'], DEFAULT_USER['email'], DEFAULT_USER['date'])
        res = self.mysql.session.query(Users).all()
        assert len(res) == 1


