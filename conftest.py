import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--url', default='https://target.my.com/')


@pytest.fixture(scope='function')
def config(request):
    url = request.config.getoption('--url')
    return {'url': url}


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    browser = webdriver.Chrome(executable_path=r'C:\Users\dlee9\OneDrive\Рабочий стол\Проги\Python\chromedriver.exe')
    browser.get(url)
    browser.maximize_window()
    yield browser
    browser.close()