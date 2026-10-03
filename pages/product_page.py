from selenium.webdriver.common.by import By
from pages.base_page import BasePage, retry_on_popup
from selenium.common.exceptions import NoSuchElementException


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.search_bar = (By.ID, "search_product")
        self.search_button = (By.ID, "submit_search")
        self.product = (By.CLASS_NAME, "product-image-wrapper")
        self.add_to_cart_buttons = (By.CSS_SELECTOR, "a.add-to-cart")
        self.continue_button = (
            By.XPATH, "//button[text()='Continue Shopping']")
        self.view_cart_button = (By.CSS_SELECTOR, "a[href='/view_cart']")

    @retry_on_popup()
    def search(self, string):
        search_input = self.driver.find_element(*self.search_bar)
        search_input.clear()
        search_input.send_keys(string)

        self.driver.find_element(*self.search_button).click()

    @retry_on_popup()
    def find_product(self):
        return self.driver.find_element(*self.product)

    @retry_on_popup()
    def add_to_cart(self):
        cart_buttons = self.driver.find_elements(*self.add_to_cart_buttons)

        if not cart_buttons:
            raise NoSuchElementException('No add to cart buttons found')

        cart_buttons[0].click()

    @retry_on_popup()
    def continue_shopping(self):
        self.driver.find_element(*self.continue_button).click()

    @retry_on_popup()
    def view_cart(self):
        self.driver.find_element(*self.view_cart_button).click()
