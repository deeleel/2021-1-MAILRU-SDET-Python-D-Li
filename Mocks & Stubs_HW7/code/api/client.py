import logging
import socket
import json

from settings import MOCK_HOST, MOCK_PORT

logger = logging.getLogger('test')


class ApiClient:

    def __init__(self, host, port):
        
        self.host = host
        self.port = int(port)

        self.mock_host = MOCK_HOST
        self.mock_port = int(MOCK_PORT)

        self.header = ''


    @staticmethod
    def log_pre(method, url, data, expected_status):
        logger.info(f'Performing {method} request:\n'
                    f'URL: {url}\n'
                    f'DATA: {data}\n\n'
                    f'expected status: {expected_status}\n\n')

    @staticmethod
    def log_post(response):
        log_str = 'Got response:\n' \
                  f'RESPONSE STATUS: {response[0].split(" ")[1]}\n'
        res = ''
        for i in response:
            res += i
            res += '\n'

        logger.info(f'{log_str}\n'
                    f'RESPONSE CONTENT: \n{res}\n')

    def connection(self, client, mock=False):
        if mock:
            client.connect((self.mock_host, self.mock_port))
            self.header = f'Host: {self.mock_host}:{self.mock_port}\r\n'
        else:
            client.connect((self.host, self.port))
            self.header = f'Host: {self.host}:{self.port}\r\n'

    def upgrate_header(self, data):
        if data:
            data = json.dumps(data)
            length = len(data)
            self.header +=  'Content-Type: application/json' \
                           f'\r\nContent-Length: {length}\r\n' \
                           f'\r\n{data}'

    def read_data(self, client):
        total_data = []
        while True:
            data = client.recv(1024)
            if data:
                total_data.append(data.decode())
            else:
                break

        response = ''.join(total_data).splitlines()

        client.close()
        return response

    def _request(self, method, location, data=None, expected_status=200, mock=False):

        self.log_pre(method, location, data, expected_status)

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        self.connection(client, mock)

        if data:
            self.upgrate_header(data)

        req = f'{method} {location} HTTP/1.1\r\n{self.header}\r\n'

        client.send(req.encode())
        response = self.read_data(client)
        
        self.log_post(response)

        return response



    def add_user(self, name):
        data = {'name': name}
        request = self._request('POST', '/add_user', data=data, expected_status=201)
        
        return request

    def get_user_by_name(self, name):
        params = f'/get_user/{name}'
        request = self._request('GET', params)

        return request

    def delete_surname(self, name):
        param = f'/delete_surname/{name}'

        request = self._request('DELETE', location=param, mock=True)
        return request

    def update_surname(self, name, new_surname):
        param = f'/update_surname/{name}'
        data = {'new_surname': new_surname}

        request = self._request('PUT', location=param, data=data, mock=True)
        return request

        
