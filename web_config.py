from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BrowserDriver:
    def __init__(self, driver):
        self.driver = driver

        if driver == "chrome":
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--window-size=1920,1200")
            chrome_options.add_argument("--disable-dev-shm-usage")
            self.driver = webdriver.Chrome()

            print(f"{driver}")

        elif driver == "firefox":
            self.driver = webdriver.Firefox()
        else:
            print(f"{driver}, is not defined")


if __name__ == "__main__":
    drive = BrowserDriver("chrome")


