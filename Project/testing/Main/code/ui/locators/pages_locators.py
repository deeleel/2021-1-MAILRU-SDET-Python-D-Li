from selenium.webdriver.common.by import By


class BasePageLocators:
    pass

class CommonLogin:
    USERNAME_INPUT = (By.CSS_SELECTOR, '#username')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#submit')
    ALERT = (By.CSS_SELECTOR, '#flash')
    ALERT_AD = (By.XPATH, '//*[@id="flash" and normalize-space(text())="{}"]')

class LoginPageLocators(CommonLogin):
    
    CREATE_ACC = (By.CSS_SELECTOR, '[href="/reg"]')

class RegistrationPageLocators(CommonLogin):

    EMAIL_INPUT = (By.CSS_SELECTOR, '#email')
    PASSWORD_REPEAT = (By.CSS_SELECTOR, '#confirm')
    ACCEPT_TERMS = (By.CSS_SELECTOR, '#term[type="checkbox"]')

    LOGIN = (By.CSS_SELECTOR, '[href="/login"]')

class DashboardPageLocators:

    LOGOUT_BUTTON = (By.CSS_SELECTOR, '.uk-button[href="/logout"]')
    NAME = (By.CSS_SELECTOR, '#login-name')

    # nav
    LINK = (By.XPATH, '//nav//*[normalize-space(text())="{}"]')
    LINKS_DROP = (By.XPATH, '//*[contains(@class, "uk-dropdown")]//*[normalize-space(text())="{}"]')

    NAME_LOCATOR = (By.XPATH, '//*[@id="login-name"]//*[normalize-space(text())="Logged as {}"]')
    ID_LOCATOR = (By.XPATH, '//*[@id="login-name"]//*[contains(normalize-space(text()),"VK ID:")]')

    CENTER_CIRCLES = (By.XPATH, '//*[normalize-space(text())="{}"]/parent::*//img')

    QUOTE = (By.XPATH, '//*[normalize-space(text())="powered by ТЕХНОАТОМ"]/following-sibling::p')

    TAB = (By.LINK_TEXT, "{}")