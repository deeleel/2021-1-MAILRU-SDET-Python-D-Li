from mysql.models import Requests, RequestTypes, PopularRequests, Err4Requests, Err5Requests
from tests.base import MySQLBase


class TestDB(MySQLBase):

    def test_all_requests(self):
        self.mysql_builder.fill_counter(self.data[0][0])
        res = self.mysql.session.query(Requests).all()

        assert len(res) == 1


    def test_types_of_request(self):
        self.mysql_builder.fill_type_of_requests(self.data[0][1])
        query = self.mysql.session.query(RequestTypes).all()

        assert len(query) == self.data[1]['types']

    def test_popular_requests(self):
        self.mysql_builder.fill_pupular_requests(self.data[0][2])
        query = self.mysql.session.query(PopularRequests).all()

        assert len(query) == self.data[1]['popular']

    def test_err4_requests(self):
        self.mysql_builder.fill_err4_requests(self.data[0][3])
        query = self.mysql.session.query(Err4Requests).all()

        assert len(query) == self.data[1]['err4']

    def test_err5_requests(self):
        self.mysql_builder.fill_err5_requests(self.data[0][4])
        query = self.mysql.session.query(Err5Requests).all()

        assert len(query) == self.data[1]['err5']



