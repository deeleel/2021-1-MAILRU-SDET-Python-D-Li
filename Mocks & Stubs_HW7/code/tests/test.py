import json

import settings
from mocks.flask_mock import SURNAME_DATA
from tests.base import ApiBase

url = f'http://{settings.APP_HOST}:{settings.APP_PORT}'


class TestApp(ApiBase):

    def test_add_get_user(self):

        name = self.builder.name()
        user_id_from_add = self.api_client.add_user(name)
        user_id_from_add = json.loads(user_id_from_add[-1])['user_id']

        user_id_from_get = self.api_client.get_user_by_name(name)
        user_id_from_get = json.loads(user_id_from_get[-1])['user_id']

        assert user_id_from_add == user_id_from_get
        

    def test_get_non_existent_user(self):

        resp = self.api_client.get_user_by_name('dnsfndksfnkjsdnfjkdsjkfnsd')
        assert resp[0].split(" ")[1] == '404'


    def test_add_existent_user(self):

        name = self.builder.name()
        self.api_client.add_user(name) 
        resp = self.api_client.add_user(name) 
        
        assert resp[0].split(" ")[1] == '400'


    def test_get_age(self):
        name = self.builder.name()

        self.api_client.add_user(name)
        resp = self.api_client.get_user_by_name(name)

        assert isinstance(json.loads(resp[-1])['age'], int)
        assert 0 <= json.loads(resp[-1])['age'] <= 100


    def test_has_surname(self):
        name = self.builder.name()
        surname = self.builder.surname()

        SURNAME_DATA[name] = surname

        self.api_client.add_user(name)

        resp = self.api_client.get_user_by_name(name)
        assert json.loads(resp[-1])['surname'] == surname


    def test_has_not_surname(self):
        name = self.builder.name()
        self.api_client.add_user(name)

        resp = self.api_client.get_user_by_name(name)
        assert json.loads(resp[-1])['surname'] == None

class TestMock(ApiBase):

    def test_delete_surname(self):
        name = self.builder.name()
        surname = self.builder.surname()

        SURNAME_DATA[name] = surname
        self.api_client.add_user(name)

        self.api_client.delete_surname(name)

        resp = self.api_client.get_user_by_name(name)
        assert json.loads(resp[-1])['surname'] == None
    

    def test_delete_non_existent_user_surname(self):
        name = self.builder.name()

        resp = self.api_client.delete_surname(name)
        assert resp[0].split(" ")[1] == '404'

    def test_delete_surname_not_existed(self):
        name = self.builder.name()

        self.api_client.add_user(name)

        resp = self.api_client.delete_surname(name)
        assert resp[0].split(" ")[1] == '404'


    def test_update_surname(self):
        name = self.builder.name()
        surname = self.builder.surname()
        surname2 = self.builder.surname()

        SURNAME_DATA[name] = surname
        self.api_client.add_user(name)

        self.api_client.update_surname(name, surname2)

        resp = self.api_client.get_user_by_name(name)
        assert json.loads(resp[-1])['surname'] == surname2


    def test_update_surname_not_existed(self):
        name = self.builder.name()
        surname2 = self.builder.surname()

        self.api_client.add_user(name)

        resp = self.api_client.update_surname(name, surname2)
        assert resp[0].split(" ")[1] == '404'
    

    def test_update_non_existent_user_surname(self):
        name = self.builder.name()
        surname = self.builder.surname()

        resp = self.api_client.update_surname(name, surname)
        assert resp[0].split(" ")[1] == '404'




