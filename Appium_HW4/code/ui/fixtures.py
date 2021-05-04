import os
import shutil

import allure
import pytest
from appium import webdriver

from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPageANDROID
from ui.pages.settings_page import SettingsPageANDROID
from ui.pages.news_page import NewsPageANDROID
from ui.pages.about_page import AboutPageANDROID

from ui.capability import capability_select


class UnsupportedDeviceType(Exception):
    pass


@pytest.fixture
def base_page(driver, config):
    return BasePage(driver=driver, config=config)


@pytest.fixture
def main_page(driver, config):
    return MainPageANDROID(driver=driver, config=config)

@pytest.fixture
def settings_page(driver, config):
    return SettingsPageANDROID(driver=driver, config=config)

@pytest.fixture
def news_page(driver, config):
    return NewsPageANDROID(driver=driver, config=config)

@pytest.fixture
def about_page(driver, config):
    return AboutPageANDROID(driver=driver, config=config)


def get_driver(device_os, appium_url):
    if device_os == 'android':
        desired_caps = capability_select(device_os)
        driver = webdriver.Remote(appium_url, desired_capabilities=desired_caps)
        return driver
    else:
        raise UnsupportedDeviceType(f' Unsupported device_os type {device_os}')


@pytest.fixture(scope='function')
def driver(config):
    device_os = config['device_os']
    appium_url = config['appium']
    browser = get_driver(device_os, appium_url)
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
