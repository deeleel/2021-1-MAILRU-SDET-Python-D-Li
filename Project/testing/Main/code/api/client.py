import logging
from urllib.parse import urljoin
import allure
import requests
from utils.test_data import DEFAULT_USER

from utils.builder import Builder


logger = logging.getLogger('test')

MAX_RESPONSE_LENGTH = 500

class ResponseErrorException(Exception):
    pass

class ResponseStatusCodeException(Exception):
    pass

class InvalidLoginException(Exception):
    pass


class ApiClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.builder = Builder()
        self.header = None



    @staticmethod
    def log_pre(method, url, headers, data):
        logger.info(f'Performing {method} request:\n'
                    f'URL: {url}\n'
                    f'HEADERS: {headers}\n'
                    f'DATA: {data}\n\n')


    @staticmethod
    def log_post(response):
        log_str = f'Got response:\n RESPONSE STATUS: {response.status_code}'

        if len(response.text) > MAX_RESPONSE_LENGTH:
            if logger.level == logging.INFO:
                logger.info(f'{log_str}\n'
                            f'RESPONSE CONTENT: COLLAPSED due to response size > {MAX_RESPONSE_LENGTH}. '
                            f'Use DEBUG logging.\n\n')
            elif logger.level == logging.DEBUG:
                logger.debug(f'{log_str}\n'
                             f'RESPONSE CONTENT: {response.text}\n\n')
        else:
            logger.info(f'{log_str}\n'
                        f'RESPONSE CONTENT: {response.text}\n\n')


    @allure.step('Making a {method} request to {location}')
    def _request(self, method, location, headers=None, data=None, json=None, files=None, params=None):

        self.log_pre(method, location, headers, data)

        response = self.session.request(method, location, headers=headers, data=data, json=json,
                                        files=files, params=params)

        self.log_post(response)

        return response


    @allure.step('Getting cookies')
    def get_cookie(self):
        self._request('GET', self.base_url)
        self.header = {'Cookie': f'session={self.session.cookies["session"]}'}


    @allure.step('Add new user({name}, {password}, {email}) request')
    def post_api_user(self, name, password, email):
        data = {
            'username':name,
            'password':password,
            'email':email
        }

        header = {'Content-Type': 'application/json'}
        header.update(self.header)
        res = self._request('POST', urljoin(self.base_url, '/api/add_user'), headers=header, data=data)
        print(res)
        print(res.text)
        return res


    @allure.step('Delete user - {name} request')    
    def delete_api_user(self, name, from_ui=False):
        if from_ui:
            self.post_login()

        req = self._request('GET', urljoin(self.base_url, f'/api/del_user/{name}'), headers=self.header)
        return req


    @allure.step('Block user - {name} request') 
    def block_api_user(self, name):
        res = self._request('GET', urljoin(self.base_url, f'/api/block_user/{name}'), headers=self.header)
        return res

    @allure.step('Unblock user - {name} request') 
    def unblock_api_user(self, name):
        res = self._request('GET', urljoin(self.base_url, f'/api/accept_user/{name}'), headers=self.header)
        return res

    @allure.step('Getting app status')
    def get_status_app(self):
        req = self._request('GET', urljoin(self.base_url, '/status'))
        return req

    @allure.step('Request to log in user {name} - {password}')
    def post_login(self, name=DEFAULT_USER['name'], password=DEFAULT_USER['password'], valid=True):
        data = {
            'username': name,
            'password': password,
            'submit': "Login" 
        }
        res = self._request('POST', urljoin(self.base_url, '/login'), data=data)
        if valid:
            self.get_cookie()
        return res

    @allure.step('Request to register user {name} - {password} - {email}')
    def post_reg(self, name, password, email, valid=True):
        data = {
            'username': name,
            'email': email,
            'password': password,
            'confirm': password,
            'term': 'y',
            'submit': "Register"
        }
        res = self._request('POST', urljoin(self.base_url, '/reg'), data=data)
        if valid:
            self.get_cookie()
        return res

    @allure.step('Creating temporary user..')
    def create_user(self):
        name = self.builder.name()
        passw = self.builder.passw()
        email = self.builder.email()

        self.post_reg(name, passw, email)
        return {'name': name, 'password': passw, 'email': email}

# Mock

    @allure.step('Request user id from Mock')
    def get_id(self, name):
        res = self._request('GET', urljoin(self.base_url, f"/vk_id/{name}"))
        return res

    @allure.step('Request to add user to Mock')
    def add_user_mock(self, name):
        res = self._request('POST', urljoin(self.base_url, f"/add_user/{name}"))
        return res



