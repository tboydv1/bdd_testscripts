from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from variables import locators
from web_config import BrowserDriver
from selenium.webdriver.support import expected_conditions as EC


class LampFrontend:
    """
        The class responsible for all activities on the frontend.
    """

    def __init__(self):
        self.site = BrowserDriver("chrome")
        self.browse = self.site.driver

    def go_to_home(self):
        self.browse.maximize_window()
        self.browse.get(locators.home)
        web = WebDriverWait(self.browse, 30)
        web.until(EC.visibility_of_element_located((By.XPATH, locators.login_page_button)))

    # def login(self, user, pswd):
    #     self.site.login(user, pswd)

    def wait_action(self, element):
        web_wait = WebDriverWait(self.browse, 30)
        web_wait.until(ec.visibility_of_element_located((By.XPATH, element)))

    def click(self, element):
        self.browse.find_element_by_xpath(element).click()

    def verify_action(self, id_, text):
        element = self.browse.find_element_by_xpath(id_)

        try:
            assert text in element.text
        except ValueError:
            print('Page load Failed!!!')


    def insert(self, field_id, search_text):
        self.browse.find_element_by_xpath(field_id).send_keys(search_text)

    def verify_any_message(self, id_,  message_list):
        element = self.browse.find_element_by_xpath(id_)

        try:
            for m in message_list:
                if m in element.text:
                    print("True --> {}", m)
                    break
            else:
                raise AssertionError
        except ValueError:
            print("False")


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
