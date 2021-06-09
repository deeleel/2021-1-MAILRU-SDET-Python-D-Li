from ui.pages.base_page import BasePage
from ui.locators.pages_locators import DashboardPageLocators
from utils.decorators import wait

import allure
import logging
logger = logging.getLogger('test')

class DashboardPage(BasePage):

    url = 'http://notmyapp:8080/welcome/'
    locators = DashboardPageLocators()

    @allure.step('Clicking on nav button {nav}')
    def click_nav(self, nav):
        button = (self.locators.LINK[0], self.locators.LINK[1].format(nav))
        self.click(button)
        logger.info(f'Clicked on {nav}')

    @allure.step('Clicking on {link} in the {nav}')
    def click_link(self, nav, link):
        main_button = self.find((self.locators.LINK[0], self.locators.LINK[1].format(nav)))
        self.action_chains.move_to_element(main_button).perform()
        
        button = (self.locators.LINKS_DROP[0], self.locators.LINKS_DROP[1].format(link))
        self.click(button)

        logger.info(f'Clicked on {link} in the {nav}')

    @allure.step('Clicking on {circle}')
    def click_circle(self, circle):
        button = (self.locators.CENTER_CIRCLES[0], self.locators.CENTER_CIRCLES[1].format(circle))
        self.click(button)

        logger.info(f'Clicked on {circle}')

    @allure.step('Logging out....')
    def logout(self):
        self.click(self.locators.LOGOUT_BUTTON)
        logger.info('Logged out....')

    @allure.step('Checking name: {name} in the header')
    def check_name(self, name):
        loc = (self.locators.NAME_LOCATOR[0], self.locators.NAME_LOCATOR[1].format(name))
        cond = self.element_exist(loc)
        logger.info(f'{name} in the nav is {cond}')
        return cond

    @allure.step('Checking id in the header')
    def check_id(self):
        cond = self.element_exist(self.locators.ID_LOCATOR)
        logger.info(f'VK_ID is in the nav')
        return cond

    @allure.step('Getting current quote')
    def get_quote(self):
        text = self.get_value(self.locators.QUOTE)
        logger.info(f'Quote is {text}')
        return text

    @allure.step('Changing tab')
    def change_tab(self):
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                logger.info(f'Changed tab')


