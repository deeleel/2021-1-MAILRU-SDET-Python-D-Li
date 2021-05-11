from mysql.models import Requests, RequestTypes, PopularRequests, Err4Requests, Err5Requests


class MySQLBuilder:

    def __init__(self, client):
        self.client = client
        
    def fill_counter(self, data):
        row = Requests(
            count = data
        )

        self.client.session.add(row)

    def fill_type_of_requests(self, data):
        for i in data:
            row = RequestTypes(
                name = i[0],
                count = i[1]
            )
            self.client.session.add(row)

    def fill_pupular_requests(self, data):
        for i in data:
            row = PopularRequests(
                url = i[0],
                count = i[1]
            )
            self.client.session.add(row)

    def fill_err4_requests(self, data):
        for i in data:
            row = Err4Requests(
                url = i[0],
                status = i[1],
                weight = i[2],
                ip = i[3]
            )
            self.client.session.add(row)

    def fill_err5_requests(self, data):
        for i in data:
            row = Err5Requests(
                ip = i[0][1],
                count = i[1]
            )
            self.client.session.add(row)
