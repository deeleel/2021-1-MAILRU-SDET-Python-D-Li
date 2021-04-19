import logging
from urllib.parse import urljoin
import json
import allure
import requests

from utils.date import get_date


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
    def _request(self, method, location, headers=None, data=None, allow_redirects=True, json=None, files=None, expected_status=200):

        self.log_pre(method, location, headers, data, expected_status)

        response = self.session.request(method, location, headers=headers, data=data, json=json, allow_redirects=allow_redirects)

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

        data = {
            'email': 'di12kli@yandex.ru',
            'password': 'simple123456',
            'continue': 'https://account.my.com/login_continue/?continue=https%3A%2F%2Faccount.my.com',
            'failure': 'https://account.my.com/login/?continue=https%3A%2F%2Faccount.my.com',
            'nosavelogin': '0'
        }

        h2 = {
            'Origin': 'https://account.my.com',
            'Referer': 'https://account.my.com/'
        }
        self._request('POST', url, headers=h2, data=data)

        res2 = self._request("GET", urljoin(self.base_url, '/dashboard'))

        assert 'data-ga-username="di12kli@yandex.ru"' in res2.text

        self.get_token()


    @allure.step('Checking id = {id} segment')
    def check_segment(self, id):
        res = self._request('GET', urljoin(self.base_url, 'api/v2/remarketing/segments.json'))
        if f'"id": {id}' in res.text:
            return True
        else: 
            return False


    @allure.step('Checking id = {id} campaign')
    def check_campaign(self, id):
        date = get_date()
        res = self._request('GET', urljoin(self.base_url, f'api/v2/statistics/campaigns/day.json?date_from={date}&date_to={date}&attribution=impression&campaign_status=active&metrics=base%2Cuniques&adv_user=10910620'))
        # print(res.text)
        # print(id)
        if f'"id":{id}' in res.text:
            return True
        else:
            return False
    
    @allure.step('Creating segment')
    def post_segment_create(self, name):

        self._request('GET', urljoin(self.base_url, 'segments/segments_list/new'))

        data = {"name": name,
                "pass_condition": 1,
                "relations": [{
                    "object_type": "remarketing_player",
                    "params": {
                        "type": "positive",
                        "left": 365,
                        "right": 0
                    }
                }],
                "logicType":"or"
            }

        segment_id = self._request('POST', urljoin(self.base_url, 'api/v2/remarketing/segments.json'), headers=self.csrf_header, json=data)
        j = json.loads(segment_id.text)

        assert self.check_segment(j['id'])

        return j['id']


    @allure.step('Creating segment and deleting it')
    def delete_segment(self, name):

        seg_id = self.post_segment_create(name)
        self._request('DELETE', urljoin(self.base_url, f'api/v2/remarketing/segments/{seg_id}.json'), headers=self.csrf_header, expected_status=204)

        assert self.check_segment(seg_id) == False


    @allure.step('Creating campaign')
    def post_create_campaign(self, file_path, name, title, text):

        data = {
                "name": name,
                "conversion_funnel_id":None,
                "objective":"traffic",
                "enable_offline_goals":False,
                "targetings":{
                    "split_audience":[1,2,3,4,5,6,7,8,9,10],
                    "sex":["male","female"],
                    "age":{"age_list":[0,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75],
                           "expand":True},
                    "geo":{"regions":[188]},
                    "interests_soc_dem":[],
                    "segments":[],
                    "interests":[],
                    "fulltime":{
                        "flags":["use_holidays_moving","cross_timezone"],
                        "mon":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
                        "tue":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
                        "wed":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
                        "thu":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
                        "fri":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
                        "sat":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
                        "sun":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
                    },
                    "pads":[102634,102643],
                    "mobile_types":["tablets","smartphones"],
                    "mobile_vendors":[],
                    "mobile_operators":[]
                },
                "age_restrictions":None,
                "date_start":None,
                "date_end":None,
                "autobidding_mode":"second_price_mean",
                "budget_limit_day":None,
                "budget_limit":None,
                "mixing":"fastest",
                "utm":None,
                "enable_utm":True,
                "price":"4.97",
                "max_price":"0",
                "package_id":1619,
                "banners":[{
                    "urls":{"primary":{"id":136898}},
                    "textblocks":{"title_25":{"text":title},
                                  "text_90":{"text":text},
                                  "cta_sites_full":{"text":"visitSite"}
                                },
                    "content":{"icon_256x256":{"id":8644887},
                               "video_square_30s":{"id":8667037}
                            },
                    "name":""
                }]
            }

        res = self._request('POST', urljoin(self.base_url, 'api/v2/campaigns.json'), headers=self.csrf_header, json=data)
        j = json.loads(res.text)
        
        assert self.check_campaign(j['id'])
        self.delete_campaign(j['id'])

        return j['id']

    
    @allure.step('Deleting campaign')
    def delete_campaign(self, id):

        data = [{"id": id,
                "status":"deleted"}]

        self._request('POST', urljoin(self.base_url, 'api/v2/campaigns/mass_action.json'), headers=self.csrf_header, json=data, expected_status=204)

        assert self.check_campaign(id) == False
