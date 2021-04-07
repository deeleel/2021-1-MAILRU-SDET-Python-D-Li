from selenium.webdriver.common.by import By


class BasePageLocators:
    pass


class LoginPageLocators:

    LOGIN_LOCATOR   = (By.XPATH, '//*[contains(text(), "Войти")]')
    LOGIN_EMAIL     = (By.NAME, 'email')
    LOGIN_PASSWORD  = (By.NAME, 'password')
    LOGIN_BUTTON    = (By.XPATH, '(//*[contains(text(), "Войти")])[2]')

    NEGATIVE_LOGIN_NAME  = (By.XPATH, '//*[normalize-space(text())="Введите email или телефон"]')
    NEGATIVE_LOGIN_NAME2 = (By.XPATH, '//*[@class="formMsg_title" and text()="Error"]')


class DashboardPageLocators:

    LOGOUT_ICON             = (By.XPATH, '//*[@class="js-head-balance"]//parent::*')
    LOGOUT_LOCATOR          = (By.XPATH, '//a[@href="/logout"]')

    PROFILE_LOCATOR         = (By.CSS_SELECTOR, 'a[href="/profile"]')
    STATISTICS_LOCATOR      = (By.CSS_SELECTOR, 'a[href="/statistics"]')
    SEGMENTS_LOCATOR        = (By.CSS_SELECTOR, 'a[href="/segments"]')

    AD_CAMPAIGN1 = (By.CSS_SELECTOR, 'a[href="/campaign/new"]')
    AD_CAMPAIGN2 = (By.XPATH, '//*[normalize-space(text())="Создать кампанию"]')

class CampaignPageLocators:
    
    GOAL_OF_CAMPAIGN        = (By.CSS_SELECTOR, '._traffic')
    LINK_TO_SITE            = (By.CSS_SELECTOR, '[data-gtm-id="ad_url_text"]')
    NAME_OF_CAMPAIGN        = (By.CSS_SELECTOR, '.input_campaign-name input')

    IMG                     = (By.XPATH, '//input[@data-test="icon_256x256"]')
    SAVE_IMG                = (By.CSS_SELECTOR, '.image-cropper__save')

    VIDEO                   = (By.XPATH, '//input[@accept=".mp4"]')
    CHECK_VIDEO_UPLOAD      = (By.XPATH, '//*[@data-pattern-name="video_square_30s_full"]//*[normalize-space(text())="Перетащите видео-файл из медиатеки или кликните для загрузки с вашего компьютера"]')

    BANNER_FORMAT           = (By.XPATH, '//*[@class="banner-format-item__title" and normalize-space(text())="Квадратное видео"]')
    HEADER                  = (By.XPATH, '//input[@placeholder="Введите заголовок объявления"]')
    TEXT                    = (By.XPATH, '//textarea[@placeholder="Введите текст объявления"]')

    SUBMIT                  = (By.XPATH, '//*[@data-class-name="Submit"]//*[@class="button__text" and normalize-space(text())="Создать кампанию"]')

    CHECK_CAMPAIGN_BY_NAME  = (By.XPATH, '//*[@data-entity-type="campaign"]//*[@title={}]')

class SegmentsPageLocators:
    
    CREATE_SEGMENT1         = (By.CSS_SELECTOR, '[href="/segments/segments_list/new/"]')
    CREATE_SEGMENT2         = (By.CSS_SELECTOR, 'button.button_submit')

    CHECKBOX                = (By.CSS_SELECTOR, '.adding-segments-source__checkbox')
    ADD_SEGMENT             = (By.XPATH, '//*[@class="adding-segments-modal"]//*[@data-class-name="Submit"]')

    INPUT_WITH_NAME         = (By.CSS_SELECTOR, '.input_create-segment-form input')
    SUBMIT_SEGMENT          = (By.XPATH, '//*[@class="create-segment-form"]//*[@data-class-name="Submit"]')
    CHECK_SEGMENT_BY_NAME   = (By.XPATH, '//*[@class="ReactVirtualized__Grid"]//*[normalize-space(text())={}]')

    SEGMENT_TM              = '(//*[@class="ReactVirtualized__Grid"]//*[@href])[1]'
    CHECK_SEGMENT           = (By.XPATH, SEGMENT_TM)
    CROSS_ICON              = (By.XPATH, SEGMENT_TM + '/parent::*/parent::*/following-sibling::*[4]//*')

    VERIFY_DELETE           = (By.CSS_SELECTOR, '.button_confirm-remove')

    