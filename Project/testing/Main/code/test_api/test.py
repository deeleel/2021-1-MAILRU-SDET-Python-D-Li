import json
import allure
import pytest

from test_api.base import ApiBase
from utils.test_data import LOGIN_DATA, REGISTER_DATA, DEFAULT_USER


class TestMock(ApiBase):

    @pytest.mark.API
    @allure.feature('Test Mock successfully')
    @allure.story('Getting user id from Mock')
    def test_get_id(self):
        """ Getting id of the default user
        1. Making request to Mock
        2. Expecting response - 200 with vk_id = 1
        """
        res = self.mock_client.get_id(DEFAULT_USER['name'])
        assert res.status_code == 200, 'Wrong status code'
        assert json.loads(res.text)['vk_id'] == DEFAULT_USER['id']


    @pytest.mark.API
    @allure.feature('Test Mock negative')
    @allure.story('Getting invalid user id from Mock')
    def test_get_id_wrong(self):
        """ Trying to ger id with invalid data
            1. Making request to Mock
            2. Expecting response - 404 with {}
        """
        name = self.builder.name()
        res = self.mock_client.get_id(name)
        assert res.status_code == 404, 'Wrong status code'
        assert json.loads(res.text) == {}


    @pytest.mark.API
    @allure.feature('Test Mock successfully')
    @allure.story('Posting new user into Mock')
    def test_add_user(self):
        """ Adding new user into Mock
            1. Making request to Mock
            2. Expecting response - {'name':name, 'vk_id': id}, 201
        """
        name = self.builder.name()
        res = self.mock_client.add_user_mock(name)
        assert res.status_code == 201, 'Wrong status code'
        assert json.loads(res.text)['name'] == name
        assert json.loads(res.text)['vk_id']


    @pytest.mark.API
    @allure.feature('Test Mock negative')
    @allure.story('Posting existing user into Mock')
    def test_add_existing_user(self):
        """ Trying to add user into Mock
        1. Making request to Mock
        2. Expecting response - , 304
        """
        res = self.mock_client.add_user_mock(DEFAULT_USER['name'])
        assert res.status_code == 304, 'Wrong status code'
        assert res.text == ''


        
class TestStatus(ApiBase):

    @pytest.mark.API
    @allure.story('Getting app status')
    def test_app_status(self):
        """ Getting app status
            1. Making api request
            2. Expecting response - {"status": "ok"}
        """
        res = self.api_client.get_status_app()
        assert json.loads(res.text)['status'] == 'ok'

  
class TestLogin(ApiBase):

    @pytest.mark.API
    @allure.feature('Test Login')
    @allure.story('Successfully logging in default user')
    def test_login(self):
        """ Logging in 
            1. Creating new user
            2. Making api request to log in
            3. Deleting new user
            4. Expecting status code = 200
        """
        cred = self.api_client.create_user()
        res = self.api_client.post_login(cred['name'], cred['password'])

        self.api_client.delete_api_user(cred['name'])
        assert res.status_code == 200, 'Wrong status code'
        assert 'Welcome!' in res.text
        

    @pytest.mark.API
    @allure.feature('Test negative Login')
    @allure.story('Testing Login with invalid data')
    @pytest.mark.parametrize('name, passw, mssg', LOGIN_DATA)
    def test_invalid_login(self, name, passw, mssg):
        """ Testing invalid login
            1. Making api request to log in with wrong data
            2. Expecting status code = 401, not authorized
        """
        res = self.api_client.post_login(name, passw, valid=False)
        assert res.status_code == 401, 'Wrong status code'


    @pytest.mark.API
    @allure.feature('Test negative Login')
    @allure.story('Testing blocked user Login')
    def test_login_blocked_user(self):
        """ Testing blocked user login
            1. Creating new user
            2. Blocking that user
            3. Trying to log in blocked user
            4. Deleting created user
            5. Expecting status code = 401, not authorized
            
        """
        cred = self.api_client.create_user()
        self.api_client.block_api_user(cred['name'])

        res = self.api_client.post_login(cred['name'], cred['password'], valid=False)

        self.api_client.delete_api_user(cred['name'])
        assert res.status_code == 401, 'Wrong status code'


  
class TestRegistration(ApiBase):

    @pytest.mark.API
    @allure.feature('Test valid Register')
    @allure.story('Test adding user via api')
    def test_add_user(self):
        """ Adding user via api
            1. Logging in as user
            2. Making request to add user via api with generated data
            3. Expecting status code = 201, created
            4. Deleting created users
        """
        cred = self.api_client.create_user()
        name = self.builder.name()
        passw = self.builder.passw()
        email = self.builder.email()

        res = self.api_client.post_api_user(name, passw, email)
        print(res.text)
        print(res.content)

        self.api_client.delete_api_user(cred['name'])
        assert res.status_code == 201,'Wrong status code'
        self.api_client.delete_api_user(name)

    
    @pytest.mark.API
    @allure.feature('Test invalid Register')
    @allure.story('Test adding user via api with invalid data')
    @pytest.mark.parametrize('name, passw, email, mssg', REGISTER_DATA)
    def test_wrong_add_user(self, name, passw, email, mssg):
        """ Adding user via api with wrong data
            1. Logging in as user
            2. Making request to add user via api with wrong data
            3. Expecting status code = 400, wrong request
        """
        cred = self.api_client.create_user()
        res = self.api_client.post_api_user(name, passw, email)
        assert res.status_code == 400, 'Wrong status code'


    @pytest.mark.API
    @allure.feature('Test valid Register')
    @allure.story('Test register user via api')
    def test_reg(self):
        """ Register user via api
            1. Making request to register user via api with generated data
            2. Expecting status code = 201, created
            3. Deleting created user
        """
        name = self.builder.name()
        passw = self.builder.passw()
        email = self.builder.email()

        res = self.api_client.post_reg(name, passw, email)

        assert res.status_code == 200, 'Wrong status code'
        assert 'Welcome!' in res.text
        self.api_client.delete_api_user(name)
        

    @pytest.mark.API
    @allure.feature('Test invalid Register')
    @allure.story('Test register user via api with wrong data')
    @pytest.mark.parametrize('name, passw, email, mssg', REGISTER_DATA)
    def test_reg_wrong(self, name, passw, email, mssg):   
        """ Register user via api with invalid data
            1. Making request to register user via api with invalid data
            2. Expecting status code = 400, wrong request
        """ 
        res = self.api_client.post_reg(name, passw, email, valid=False)

        assert res.status_code == 400, 'Wrong status code'
        assert 'Welcome!' not in res.text


 
class TestDeleting(ApiBase):

    @pytest.mark.API
    @allure.feature('Test Delete user')
    @allure.story('Testing successfull delete')
    def test_delete_user(self):
        """ Deleting user via api
            1. Creating user
            2. Making request to delete that user
            3. Expecting status code = 204, deleted
        """
        cred = self.api_client.create_user()

        res = self.api_client.delete_api_user(cred['name'])
        assert res.status_code == 204, 'Wrong status code'


    @pytest.mark.API
    @allure.feature('Test negative Delete')
    @allure.story('Testing delete non existing user')
    def test_delete_user_not_existed(self):
        """ Deleting user via api
            1. Creating user
            2. Generating name 
            3. Making request to delete user with generated name
            4. Expecting status code = 404, not found
        """
        self.api_client.create_user()
        name = self.builder.name()
        
        res = self.api_client.delete_api_user(name)
        assert res.status_code == 404, 'Wrong status code'


  
class TestBlocking(ApiBase):

    @allure.story('Testing successfull block')
    @allure.feature('Test Blocking users')
    @pytest.mark.API
    def test_block_user(self):
        """ Blocking user via api
            1. Creating user
            2. Making request to block that user
            3. Expecting status code = 200, success
            4. Deleting created user
        """
        cred = self.api_client.create_user()

        res = self.api_client.block_api_user(cred['name'])

        cred2 = self.api_client.create_user()
        self.api_client.delete_api_user(cred['name'])
        self.api_client.delete_api_user(cred2['name'])
        assert res.status_code == 200, 'Wrong status code'


    @allure.feature('Test Blocking users')
    @allure.story('Testing block non existent user')
    def test_block_user_not_existed(self):
        """ Blocking invalid user via api
            1. Creating user
            2. Making request to block user with generated name
            3. Expecting status code = 404, not found
            4. Deleting created user
        """
        cred = self.api_client.create_user()
        name = self.builder.name()

        res = self.api_client.block_api_user(name)
        
        self.api_client.delete_api_user(cred['name'])
        assert res.status_code == 404, 'Wrong status code'


    @allure.feature('Test Blocking users')
    @allure.story('Testing block blocked user')
    def test_block_blocked_user(self):
        """ Blocking blocked user via api
            1. Creating user
            2. Making request to block that user
            3. Expecting status code = 304, not changed
            4. Deleting created users
        """
        cred = self.api_client.create_user()
        self.api_client.block_api_user(cred['name'])

        cred2 = self.api_client.create_user()
        res = self.api_client.block_api_user(cred['name'])

        self.api_client.delete_api_user(cred['name'])
        self.api_client.delete_api_user(cred2['name'])
        assert res.status_code == 304, 'Wrong status code'


    @allure.feature('Test Unblocking users')
    @allure.story('Testing successfull unblock')
    def test_unblock_user(self):
        """ Unblocking user via api
            1. Creating user
            2. Making api request to block that user
            3. Creating second user
            4. Making request to unblock blocked user
            5. Expecting status code = 200, success
            6. Deleting created users
        """
        cred = self.api_client.create_user()
        self.api_client.block_api_user(cred['name'])
        cred2 = self.api_client.create_user()

        res = self.api_client.unblock_api_user(cred['name'])

        self.api_client.delete_api_user(cred['name'])
        self.api_client.delete_api_user(cred2['name'])
        assert res.status_code == 200, 'Wrong status code'


    @allure.feature('Test Unblocking users')
    @allure.story('Testing unblock non existent user')
    def test_unblock_user_not_existed(self):
        """ Unblocking user via api
            1. Creating user
            2. Making api request to unblock user with generated name
            3. Expecting status code = 404, not found
            4. Deleting created user
        """
        cred = self.api_client.create_user()
        name = self.builder.name()

        res = self.api_client.unblock_api_user(name)

        self.api_client.delete_api_user(cred['name'])
        assert res.status_code == 404, 'Wrong status code'


    @allure.feature('Test Unlocking users')
    @allure.story('Testing unblock not blocked user')
    def test_unblock_user_not_blocked(self):
        """ Unblocking user via api
            1. Creating user
            2. Making api request to unblock that user
            3. Expecting status code = 304, not changed
            4. Deleting created user
        """
        cred = self.api_client.create_user()

        res = self.api_client.unblock_api_user(cred['name'])

        self.api_client.delete_api_user(cred['name'])
        assert res.status_code == 304, 'Wrong status code'



    


