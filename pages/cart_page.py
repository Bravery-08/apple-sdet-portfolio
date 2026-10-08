from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage, retry_on_popup


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.product = (By.ID, "product-2")
        self.remove = (By.CSS_SELECTOR, "a.cart_quantity_delete")
        self.quantity = (
            By.XPATH, "//td[@class='cart_quantity']/child::button")

    @retry_on_popup()
    def find_product(self):
        return self.driver.find_element(*self.product)

    @retry_on_popup()
    def remove_first_product(self):
        self.wait.until(
            EC.element_to_be_clickable(self.remove)
        ).click()
        self.wait.until(
            EC.invisibility_of_element(self.product)
        )

    @retry_on_popup()
    def get_first_quantity(self):
        quantities = self.wait.until(
            EC.presence_of_all_elements_located(self.quantity)
        )
        return quantities[0].text
