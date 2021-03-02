from selenium import webdriver


class BrowserDriver:
    def __init__(self, driver):
        self.driver = driver

        if driver == "chrome":
            self.driver = webdriver.Chrome()
            print(f"{driver}")

        elif driver == "firefox":
            self.driver = webdriver.Firefox()
        else:
            print(f"{driver}, is not defined")


if __name__ == "__main__":
    drive = BrowserDriver("chrome")


