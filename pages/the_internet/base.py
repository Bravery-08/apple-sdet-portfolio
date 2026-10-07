from selenium.webdriver.support.ui import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
