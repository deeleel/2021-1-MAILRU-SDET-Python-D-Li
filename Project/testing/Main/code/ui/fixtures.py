import os
import allure
import pytest

from selenium import webdriver
from selenium.webdriver import ChromeOptions

from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from api.client import ApiClient

import settings

class UnsupportedBrowserType(Exception):
    pass


# API
@pytest.fixture
def api_client(config):
    return ApiClient(config['url'])

# MOCK
@pytest.fixture
def mock_client():
    return ApiClient(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}')

# UI PAGES
@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)

@pytest.fixture(scope='function')
def login_page(driver):
    return LoginPage(driver=driver)


def get_driver(config):
    browser_name = config['browser']
    selenoid = config['selenoid']
    vnc = config['vnc']

    if browser_name == 'chrome':
        options = ChromeOptions()

        options.add_experimental_option("prefs", {"download.default_directory": '/home/selenoid/Downloads'})
        options.add_experimental_option("prefs", {"profile.default_content_settings.popups": 0})
        options.add_experimental_option("prefs", {"download.prompt_for_download": False})
        caps = {'browserName': browser_name, # container spec
                'version': '89.0',
                'sessionTimeout': '2m'}

        if vnc:
            caps['version'] += '_vnc'
            caps['enableVNC'] = True

        browser = webdriver.Remote(selenoid + '/wd/hub', options=options, desired_capabilities=caps)
            
    else:
        raise UnsupportedBrowserType(f' Unsupported browser {browser_name}')

    return browser


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    browser = get_driver(config)

    browser.get(url)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def ui_report(driver, request, test_dir):
    failed_tests_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_tests_count:
        screenshot_file = os.path.join(test_dir, 'failure.png')
        driver.get_screenshot_as_file(screenshot_file)
        allure.attach.file(screenshot_file, 'failure.png', attachment_type=allure.attachment_type.PNG)

        browser_logfile = os.path.join(test_dir, 'browser.log')
        with open(browser_logfile, 'w') as f:
            for i in driver.get_log('browser'):
                f.write(f"{i['level']} - {i['source']}\n{i['message']}\n\n")

        with open(browser_logfile, 'r') as f:
            allure.attach(f.read(), 'browser.log', attachment_type=allure.attachment_type.TEXT)


@pytest.fixture(scope='session', autouse=True)
def add_allure_environment_property(request, config):
   
    alluredir = request.config.getoption('--alluredir')
    if alluredir:
        env_props = dict()
        env_props['App'] = 'myapp'
        env_props['Browser'] = config['browser']
        if config['browser'] == 'chrome':
            env_props['version'] = '89.0'
            
        if not os.path.exists(alluredir):
            os.makedirs(alluredir)
        allure_env_path = os.path.join(alluredir, 'environment.properties')

        with open(allure_env_path, 'w') as f:
            for key, value in list(env_props.items()):
                f.write(f'{key}={value}\n')