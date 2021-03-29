from selenium.webdriver.common.by import By

LOGIN_LOCATOR   = (By.XPATH, '//*[contains(text(), "Войти")]')
LOGIN_EMAIL     = (By.NAME, 'email')
LOGIN_PASSWORD  = (By.NAME, 'password')
LOGIN_BUTTON    = (By.XPATH, '(//*[contains(text(), "Войти")])[2]')

LOGOUT_ICON     = (By.XPATH, '//*[@class="js-head-balance"]//parent::*')
LOGOUT_LOCATOR  = (By.XPATH, '//a[@href="/logout"]')

PROFILE_LOCATOR = (By.CSS_SELECTOR, 'a[href="/profile"]')
PROFILE_FIO     = (By.CSS_SELECTOR, 'div[data-name="fio"] input')
PROFILE_PHONE   = (By.CSS_SELECTOR, 'div[data-name="phone"] input')
PROFILE_EMAIL   = (By.CSS_SELECTOR, 'div.js-additional-email input')
PROFILE_SUBMIT  = (By.CSS_SELECTOR, '[data-class-name="Submit"]')

PAGE1_LOCATOR   = (By.CSS_SELECTOR, 'a[href="/statistics"]')
SUCCESS1        = (By.CSS_SELECTOR, '.statistic-page-nt__no-active-campaigns-text')

PAGE2_LOCATOR   = (By.CSS_SELECTOR, 'a[href="/segments"]')
SUCCESS2        = (By.XPATH, '//*[@class="left-nav__group__label" and text()="Аудиторные сегменты"]')

