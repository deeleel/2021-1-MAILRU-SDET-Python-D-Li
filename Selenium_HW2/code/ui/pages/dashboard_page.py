from ui.pages.base_page import BasePage
from ui.locators.pages_locators import DashboardPageLocators
from ui.pages.campaign_page import CampaignPage
from ui.pages.segments_page import SegmentsPage
import allure

class DashboardPage(BasePage):

    url = 'https://target.my.com/dashboard'
    locators = DashboardPageLocators()

    @allure.step('Going to campaign page')
    def go_to_campaign(self):
        if self.element_exist(self.locators.AD_CAMPAIGN1):
            self.click(self.locators.AD_CAMPAIGN1)
        else: 
            self.click(self.locators.AD_CAMPAIGN2)
        return CampaignPage(self.driver)

    @allure.step('Going to segments page')
    def go_to_segments(self):
        self.click(self.locators.SEGMENTS_LOCATOR)
        return SegmentsPage(self.driver)