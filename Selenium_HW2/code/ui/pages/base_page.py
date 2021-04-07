import time
import logging
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from ui.locators.pages_locators import BasePageLocators

from utils.decorators import wait

CLICK_RETRY = 3
BASE_TIMEOUT = 5

class PageNotLoadedException(Exception):
    pass

logger = logging.getLogger('test')


class BasePage(object):

    url = 'https://target.my.com/'
    locators = BasePageLocators()

    def __init__(self, driver):
        self.driver = driver
        logger.info(f'{self.__class__.__name__} page is opening...')
        assert self.is_opened()

    def is_opened(self, err_locator=None):
        def _check_url():
            if self.driver.current_url != self.url:
                raise PageNotLoadedException(
                    f'{self.url} did not open in {BASE_TIMEOUT} sec for {self.__class__.__name__}.\n'
                    f'Current url: {self.driver.current_url}.')
            return True
        return _check_url()
        return wait(_check_url, error=PageNotLoadedException, check=True, timeout=BASE_TIMEOUT, interval=0.1)

    def wait(self, timeout=None):
        if timeout is None:
            timeout = BASE_TIMEOUT
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @property
    def action_chains(self):
        return ActionChains(self.driver)


    def scroll_to(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    def search(self, query):
        search = self.find(self.locators.QUERY_LOCATOR)
        search.clear()
        search.send_keys(query)
        self.click(self.locators.GO_LOCATOR)

    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                element = self.find(locator, timeout=timeout)
                self.scroll_to(element)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def element_exist(self, locator):
        try:
            self.find(locator, timeout=BASE_TIMEOUT)
        except:
            return False
        return True

    def get_value(self, locator):
        elem = self.find(locator)
        return elem.text

    def get_attr_value(self, locator, attr):
        elem = self.find(locator)
        return elem.get_attribute(attr)
