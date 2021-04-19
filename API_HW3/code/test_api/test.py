from test_api.base import ApiBase
import allure
import pytest 


class TestApi(ApiBase):
    authorize = False

    @allure.feature('API tests')
    @allure.story('Test login')
    @allure.description("""Test login with existing user/password""")
    @pytest.mark.API
    def test_valid_login(self):
        self.api_client.post_login()

class Test_Campaign(ApiBase):

    @allure.feature('API tests')
    @allure.story('Test campaign')
    @allure.description("""Creating campaign""")
    @pytest.mark.API
    def test_create_campaign(self, file_path):
        inputs = self.builder.campaign_inputs()
        self.api_client.post_create_campaign(file_path, name=inputs[0], title=inputs[1], text=inputs[2])


class Test_Segment(ApiBase):

    @allure.feature('API tests')
    @allure.story('Test Segment')
    @allure.description("""Creating segment""")
    @pytest.mark.API
    def test_create_segment(self):
        name = self.builder.segment_inputs()
        self.api_client.post_segment_create(name)

    @allure.feature('API tests')
    @allure.story('Test Segment')
    @allure.description("""Deleting segment""")
    @pytest.mark.API
    def test_delete_segment(self):
        name = self.builder.segment_inputs()
        self.api_client.delete_segment(name)

