from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from web_config import BrowserDriver
from variables import locators


class Login:
    """
        This is the login file and it is designed to
        accept credentials based on permissions
    """

    def __init__(self):
        self.site = BrowserDriver("chrome")
        self.browse = self.site.driver

    def login(self, user, pswd):
        self.browse.maximize_window()
        self.browse.get(locators.home)
        web = WebDriverWait(self.browse, 30)
        web.until(EC.visibility_of_element_located((By.XPATH, locators.login_page_button)))
        self.browse.find_element_by_xpath(locators.login_page_button).click()
        web.until(EC.visibility_of_element_located((By.XPATH, locators.login_button)))
        self.browse.find_element_by_xpath(locators.email_field).send_keys(user)
        self.browse.find_element_by_xpath(locators.password_field).send_keys(pswd)
        self.browse.find_element_by_xpath(locators.login_button).click()
        web.until(EC.visibility_of_element_located((By.XPATH, locators.user_name_heading)))

# class Login:
#     """
#     This is the login file and it is designed to accept credentials
#     base on user roles
#     """
#
#     def __int__(self):
#         self.browser = BrowserDriver("chrome")
#         self.browse = self.browser.driver
#
#     def login(self, email, password):
#         self.browse.maximize_window()
#         self.browse.driver.get(locators.home)
#
#         web = WebDriverWait(self.browse, 30)
#         web.until(EC.visibility_of_element_located((By.XPATH, locators.login_button)))
#         self.browse.find_element_by_xpath(locators.login_page_button).click()
#
#         web.until(EC.visibility_of_element_located((By.XPATH, locators.login_button)))
#
#         # # Insert email address
#         self.browse.driver.find_element_by_xpath(locators.email_field).send_keys(email)
#
#         # # Insert a password
#         self.browse.driver.find_element_by_xpath(locators.password_field).send_keys(password)
#
#         self.browse.driver.find_element_by_xpath(locators.login_button).click()
#         web.until(EC.visibility_of_element_located((By.XPATH, locators.user_name_heading)))
#
