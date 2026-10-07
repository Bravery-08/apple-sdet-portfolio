from selenium.webdriver.common.by import By
from pages.base_page import BasePage, retry_on_popup


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.signup_login_link = (By.LINK_TEXT, "Signup / Login")
        self.products_link = (By.CSS_SELECTOR, "a[href='/products']")

    @retry_on_popup()
    def go_to_login(self):
        self.driver.find_element(*self.signup_login_link).click()

    @retry_on_popup()
    def go_to_products(self):
        self.driver.find_element(*self.products_link).click()
