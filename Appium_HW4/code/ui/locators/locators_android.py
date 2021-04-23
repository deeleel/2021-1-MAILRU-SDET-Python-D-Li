from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class BasePageANDROIDLocators:
    pass  


class MainPageANDROIDLocators(BasePageANDROIDLocators):

    KEYBOARD_BUTTON = (MobileBy.ID, 'ru.mail.search.electroscope:id/keyboard')
    KEYBOARD_INPUT = (MobileBy.ID, 'ru.mail.search.electroscope:id/input_text')
    INPUT_BUTTON = (MobileBy.ID, 'ru.mail.search.electroscope:id/text_input_action')

    CARD_CONTAINS = (By.XPATH, '//*[@resource-id="ru.mail.search.electroscope:id/item_dialog_fact_card_content_block"]//*[contains(@text, "{}")]')
    MESSAGE = (By.XPATH, '//*[@resource-id="ru.mail.search.electroscope:id/dialog_item" and @text = "{}"]')
    TRACK_NAME = (By.XPATH, '//*[@resource-id="ru.mail.search.electroscope:id/player_track_name" and @text = "{}"]')

    SUGGEST_LIST = (MobileBy.ID, 'ru.mail.search.electroscope:id/suggests_list')
    SUGGEST_ITEM = (By.XPATH, '//*[@resource-id="ru.mail.search.electroscope:id/item_suggest_text" and @text = "{}"]')
    BURGER_MENU = (MobileBy.ID, 'ru.mail.search.electroscope:id/assistant_menu_bottom')


class SettingsPageANDROIDLocators(BasePageANDROIDLocators):

    NEWS_BUTTON = (MobileBy.ID, 'ru.mail.search.electroscope:id/user_settings_field_news_sources')
    ABOUT_PROGRAM_BUTTON = (MobileBy.ID, 'ru.mail.search.electroscope:id/user_settings_about')


class NewsPageANDROIDLocators:

    CHOOSE_NEWS = (By.XPATH, '//*[@resource-id="ru.mail.search.electroscope:id/news_sources_item_title" and @text = "{}"]')
    SELECTED_ITEM = (By.XPATH, '//android.widget.TextView[@text = "{}"]/following-sibling::*[@resource-id="ru.mail.search.electroscope:id/news_sources_item_selected"]')

class AboutPageANDROIDLocators:

    VERSION = (By.XPATH, '//*[@resource-id="ru.mail.search.electroscope:id/about_version" and contains(@text, "{}")]')
    COPYRIGHT = (By.XPATH, '//*[@resource-id="ru.mail.search.electroscope:id/about_copyright" and contains(@text, "{}")]')