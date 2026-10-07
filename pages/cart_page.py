from selenium.webdriver.common.by import By
from pages.base_page import BasePage, retry_on_popup


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.product = (By.ID, "product-2")

    @retry_on_popup()
    def find_product(self):
        return self.driver.find_element(*self.product)
