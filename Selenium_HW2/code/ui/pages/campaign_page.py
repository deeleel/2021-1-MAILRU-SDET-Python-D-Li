from ui.pages.base_page import BasePage
from ui.locators.pages_locators import CampaignPageLocators

import allure

class CampaignPage(BasePage):

    url = 'https://target.my.com/campaign/new'
    locators = CampaignPageLocators()

    @allure.step('Creating campaign and checking that its created')
    def create_campaign(self, file_path):
        # set up goal
        goal = self.find(self.locators.GOAL_OF_CAMPAIGN)
        self.click(self.locators.GOAL_OF_CAMPAIGN)

        # send link
        link = self.find(self.locators.LINK_TO_SITE)
        link.send_keys('https://mail.ru/')

        # get name
        self.find(self.locators.NAME_OF_CAMPAIGN)
        name = self.get_attr_value(self.locators.NAME_OF_CAMPAIGN, 'value')

        # choose banner
        banner = self.find(self.locators.BANNER_FORMAT)
        self.scroll_to(banner)
        self.click(self.locators.BANNER_FORMAT)

        # upload img
        img = self.find(self.locators.IMG)
        self.scroll_to(img)
        img.send_keys(file_path[0])
        self.click(self.locators.SAVE_IMG)

        # upload video
        video = self.find(self.locators.VIDEO)
        video.send_keys(file_path[1])

        # send header
        header = self.find(self.locators.HEADER)
        header.send_keys("sit voluptatem")

        # send text
        text = self.find(self.locators.TEXT)
        text.send_keys("Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam")

        while self.element_exist(self.locators.CHECK_VIDEO_UPLOAD):
            pass
        self.click(self.locators.SUBMIT)

        # check created campaign by unique name
        check_name = (self.locators.CHECK_CAMPAIGN_BY_NAME[0], self.locators.CHECK_CAMPAIGN_BY_NAME[1].format(name))
        
        return self.element_exist(check_name)
