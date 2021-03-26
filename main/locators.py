from selenium.webdriver.common.by import By

LOGIN_LOCATOR = (By.CSS_SELECTOR, 'div.responseHead-module-button-1BMAy4')
LOGIN_EMAIL = (By.NAME, 'email')
LOGIN_PASSWORD = (By.NAME, 'password')
LOGIN_BUTTON = (By.CSS_SELECTOR, '.authForm-module-button-2G6lZu')

LOGOUT_ICON = (By.CSS_SELECTOR, '.right-module-userNameWrap-34ibLS')
LOGOUT_LOCATOR = (By.CSS_SELECTOR, 'a[href="/logout"]')

PROFILE_LOCATOR = (By.CSS_SELECTOR, 'a[href="/profile"]')
PROFILE_FIO = (By.CSS_SELECTOR, 'div[data-name="fio"] input')
PROFILE_PHONE = (By.CSS_SELECTOR, 'div[data-name="phone"] input')
PROFILE_EMAIL = (By.CSS_SELECTOR, 'div.js-additional-email input')
PROFILE_SUBMIT = (By.CSS_SELECTOR, '[data-class-name="Submit"]')

PAGE1_LOCATOR = (By.CSS_SELECTOR, 'a.center-module-statistics-26_XmT')
PAGE2_LOCATOR = (By.CSS_SELECTOR, 'a.center-module-segments-3y1hDo')
