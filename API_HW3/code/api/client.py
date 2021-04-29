import logging
from urllib.parse import urljoin, quote_plus
import allure
import requests

from utils.date import get_date
from utils.data import get_data_campaign, get_data_segment_create


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

        self.csrf_header = None


    @staticmethod
    def log_pre(method, url, headers, data, expected_status):
        logger.info(f'Performing {method} request:\n'
                    f'URL: {url}\n'
                    f'HEADERS: {headers}\n'
                    f'DATA: {data}\n\n'
                    f'expected status: {expected_status}\n\n')


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
    def _request(self, method, location, headers=None, data=None, allow_redirects=True, json=None, files=None, params=None, expected_status=200):

        self.log_pre(method, location, headers, data, expected_status)

        response = self.session.request(method, location, headers=headers, data=data, json=json,
                                        files=files, params=params, allow_redirects=allow_redirects)

        self.log_post(response)

        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.reason} for URL "{location}"!\n'
                                              f'Expected status_code: {expected_status}.')

        return response


    @allure.step('Getting a csrf token')
    def get_token(self):
        self._request('GET', urljoin(self.base_url, 'csrf/'))
        self.csrf_header = {'X-CSRFToken': self.session.cookies['csrftoken']}


    @allure.step('Logging in via api')
    def post_login(self, user="di12kli@yandex.ru", password="simple123456"):
        url = 'https://auth-ac.my.com/auth'

        data_login = {
            'email': user,
            'password': password,
            'continue': f'https://account.my.com/login_continue/?continue=https{quote_plus("://account.my.com")}',
            'failure': f'https://account.my.com/login/?continue=https{quote_plus("://account.my.com")}',
            'nosavelogin': '0'
        }

        headers_login = {
            'Origin': 'https://account.my.com',
            'Referer': 'https://account.my.com/'
        }

        self._request('POST', url, headers=headers_login, data=data_login)
        self._request("GET", urljoin(self.base_url, '/dashboard'), expected_status=200)

        self.get_token()


    @allure.step('Checking id = {id} segment')
    def check_segment(self, id):
        res = self._request('GET', urljoin(self.base_url, 'api/v2/remarketing/segments.json')).json()
        segment = [s['id'] for s in res['items'] if s['id'] == id]

        return len(segment) == 1


    @allure.step('Checking id = {id} campaign')
    def check_campaign(self, id):
        date = get_date()
        params_campaign = {
            'date_from': date,
            'date_to': date,
            'attribution': 'impression',
            'campaign_status': 'active',
            'metrics': 'base,uniques',
            'adv_user': 10910620
        }
        res = self._request('GET', urljoin(self.base_url, 'api/v2/statistics/campaigns/day.json'),
                                                                params=params_campaign).json()
        campaign = [c['id'] for c in res['items'] if c['id'] == id]

        return len(campaign) == 1


    @allure.step('Creating segment')
    def post_segment_create(self, name):
        self._request('GET', urljoin(self.base_url, 'segments/segments_list/new'))

        data = get_data_segment_create(name)
        segment_id = self._request('POST', urljoin(self.base_url, 'api/v2/remarketing/segments.json'),
                                                            headers=self.csrf_header, json=data).json()
        assert self.check_segment(segment_id['id'])
        return segment_id['id']


    @allure.step('Creating segment and deleting it')
    def delete_segment(self, id):
        self._request('DELETE', urljoin(self.base_url, f'api/v2/remarketing/segments/{id}.json'),
                                                            headers=self.csrf_header, expected_status=204)
        assert not self.check_segment(id)


    @allure.step('Getting image id')
    def get_img_id(self, file_path):
        file = open(file_path[0], 'rb')
        files_img = {'file': file}
        data_img = {"width":0,"height":0}
        img_id = self._request('POST', urljoin(self.base_url, 'api/v2/content/static.json'), headers=self.csrf_header,
                               data=data_img, files=files_img).json()
        return img_id['id']


    @allure.step('Getting video id')
    def get_video_id(self, file_path):
        file = open(file_path[1], 'rb')
        files_v = {'file': file}
        data_v = {"width": 0, "height": 0}
        v_id = self._request('POST', urljoin(self.base_url, 'api/v2/content/video.json'), headers=self.csrf_header,
                               data=data_v, files=files_v).json()
        return v_id['id']

    @allure.step('Getting banner id')
    def get_banner_id(self):
        params_url = {'url': 'mail.ru'}
        res = self._request('GET', urljoin(self.base_url, 'api/v1/urls'), params=params_url).json()

        return res['id']


    @allure.step('Creating campaign')
    def post_create_campaign(self, file_path, name, title, text):

        img_id = self.get_img_id(file_path)
        v_id = self.get_video_id(file_path)
        banner_id = self.get_banner_id()
        data = get_data_campaign(name, title, text, img_id, v_id, banner_id)

        response_campaign = self._request('POST', urljoin(self.base_url, 'api/v2/campaigns.json'), headers=self.csrf_header, json=data).json()
        
        assert self.check_campaign(response_campaign['id'])
        self.delete_campaign(response_campaign['id'])

    
    @allure.step('Deleting campaign')
    def delete_campaign(self, id):
        data = [{"id": id,
                "status":"deleted"}]

        self._request('POST', urljoin(self.base_url, 'api/v2/campaigns/mass_action.json'), headers=self.csrf_header,
                                                                            json=data, expected_status=204)
        assert self.check_campaign(id) == False
