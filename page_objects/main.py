from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from variables import locators
from page_objects.login import Login


class LampFrontend:
    """
        The class responsible for all activities on the frontend.
    """

    def __init__(self):
        self.site = Login()

    def login(self, user, pswd):
        self.site.login(user, pswd)

    def click_trainees_tab(self):
        web_wait = WebDriverWait(self.site.browse, 30)
        self.site.browse.find_element_by_xpath(locators.trainees_tab).click()
        web_wait.until(ec.element_to_be_clickable((By.XPATH, locators.trainees_page_heading)))

    def verify_page(self, id_, text):
        element = self.site.browse.find_element_by_xpath(id_)

        try:
            assert text in element.text
            print('Page is loaded successfully')
        except ValueError:
            print('Page load Failed!!!')

# class LampFrontend:
#     """
#         The class responsible for all activities on the frontend
#     """
#
#     def __int__(self):
#         self.site = Login()
#
#     def login_as_admin(self, user, password):
#         self.site.login(user, password)
#
#     def click_trainees_tab(self):
#         web_wait = WebDriverWait(self.site.browse, 30)
#         self.site.browse.find_element_by_xpath(locators.trainees_tab).click()
#         web_wait.until(ec.element_to_be_clickable((By.XPATH, locators.trainees_tab_heading)))
