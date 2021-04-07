from ui.pages.base_page import BasePage
from ui.locators.pages_locators import SegmentsPageLocators

import allure

class SegmentsPage(BasePage):
    url = 'https://target.my.com/segments/segments_list'
    locators = SegmentsPageLocators()

    @allure.step('Creating segment and checking that its created')
    def createSeg(self):
        if self.element_exist(self.locators.CHECK_SEGMENT):
            self.click(self.locators.CREATE_SEGMENT2)
        else:
            self.click(self.locators.CREATE_SEGMENT1)

        self.click(self.locators.CHECKBOX)
        self.click(self.locators.ADD_SEGMENT)

        name = self.get_attr_value(self.locators.INPUT_WITH_NAME, "value")
        self.click(self.locators.SUBMIT_SEGMENT)

        check_name = (self.locators.CHECK_SEGMENT_BY_NAME[0], self.locators.CHECK_SEGMENT_BY_NAME[1].format(name))
        if self.element_exist(check_name):
            return True
        else: 
            return False


    @allure.step('Deleting and checking that its deleted')
    def deleting(self):
        segment_name = self.get_value(self.locators.CHECK_SEGMENT)

        self.click(self.locators.CROSS_ICON)
        self.click(self.locators.VERIFY_DELETE)

        check_name = (self.locators.CHECK_SEGMENT_BY_NAME[0], self.locators.CHECK_SEGMENT_BY_NAME[1].format(segment_name))
        if self.element_exist(check_name):
            return False
        else:
            return True





    